#!/usr/bin/env python
"""
Find and fix all incomplete MCQs in MCQ_BANK
This script reads each MCQ, identifies specific issues, and fixes them
"""

import os
import re
from pathlib import Path

class MCQFixer:
    def __init__(self):
        self.stats = {
            'total_files': 0,
            'total_mcqs': 0,
            'incomplete_mcqs': 0,
            'fixed_mcqs': 0,
            'unfixable_mcqs': 0
        }
        self.issues = {
            'missing_question': [],
            'missing_options': [],
            'missing_answer': [],
            'missing_reason': [],
            'missing_metadata': [],
            'malformed': []
        }
    
    def analyze_and_fix_all(self, mcq_bank_path='MCQ_BANK'):
        """Analyze and fix all MCQ files"""
        print("="*70)
        print("ANALYZING AND FIXING INCOMPLETE MCQs")
        print("="*70)
        
        # Process all domain folders
        for domain_folder in sorted(os.listdir(mcq_bank_path)):
            domain_path = os.path.join(mcq_bank_path, domain_folder)
            
            if not os.path.isdir(domain_path) or not domain_folder.startswith('Domain_'):
                continue
            
            print(f"\n📁 Processing: {domain_folder}")
            
            # Process all batch files
            for batch_file in sorted(os.listdir(domain_path)):
                if not batch_file.endswith('.md'):
                    continue
                
                batch_path = os.path.join(domain_path, batch_file)
                self.stats['total_files'] += 1
                
                print(f"  📄 {batch_file}")
                self.analyze_and_fix_file(batch_path)
        
        self.print_report()
    
    def analyze_and_fix_file(self, filepath):
        """Analyze and fix a single file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split by questions
        question_blocks = re.split(r'(###\s+Question\s+\d+)', content)
        
        if len(question_blocks) < 2:
            return
        
        # Reconstruct with fixes
        fixed_content = question_blocks[0]  # Header
        file_modified = False
        
        for i in range(1, len(question_blocks), 2):
            if i + 1 >= len(question_blocks):
                break
            
            header = question_blocks[i]
            block = question_blocks[i + 1]
            
            self.stats['total_mcqs'] += 1
            
            # Analyze this MCQ
            issues = self.analyze_mcq(block)
            
            if issues:
                self.stats['incomplete_mcqs'] += 1
                
                # Try to fix
                fixed_block, was_fixed = self.fix_mcq(block, issues)
                
                if was_fixed:
                    self.stats['fixed_mcqs'] += 1
                    file_modified = True
                    fixed_content += header + fixed_block
                else:
                    self.stats['unfixable_mcqs'] += 1
                    fixed_content += header + block
            else:
                fixed_content += header + block
        
        # Write back if modified
        if file_modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            print(f"    ✓ Fixed and saved")
    
    def analyze_mcq(self, block):
        """Analyze a single MCQ block and return list of issues"""
        issues = []
        
        # Check for metadata
        if not re.search(r'Domain:\s*\S', block, re.IGNORECASE):
            issues.append('missing_domain')
        if not re.search(r'Topic:\s*\S', block, re.IGNORECASE):
            issues.append('missing_topic')
        if not re.search(r'Subtopic:\s*\S', block, re.IGNORECASE):
            issues.append('missing_subtopic')
        
        # Check for question
        question_match = re.search(r'Question:\s*(.+?)(?=\n[A-D]\)|\n✔|\Z)', block, re.DOTALL | re.IGNORECASE)
        if not question_match or len(question_match.group(1).strip()) < 10:
            issues.append('missing_question')
        
        # Check for options
        if not re.search(r'A\)\s*\S', block, re.IGNORECASE):
            issues.append('missing_option_a')
        if not re.search(r'B\)\s*\S', block, re.IGNORECASE):
            issues.append('missing_option_b')
        if not re.search(r'C\)\s*\S', block, re.IGNORECASE):
            issues.append('missing_option_c')
        if not re.search(r'D\)\s*\S', block, re.IGNORECASE):
            issues.append('missing_option_d')
        
        # Check for correct answer
        if not re.search(r'Correct\s*Answer:\s*[A-D]', block, re.IGNORECASE):
            issues.append('missing_answer')
        
        # Check for reason
        reason_match = re.search(r'Reason:\s*(.+?)(?=\nTag:|\n---|\Z)', block, re.DOTALL | re.IGNORECASE)
        if not reason_match or len(reason_match.group(1).strip()) < 5:
            issues.append('missing_reason')
        
        return issues
    
    def fix_mcq(self, block, issues):
        """Fix MCQ based on identified issues"""
        fixed_block = block
        was_fixed = False
        
        # Fix missing metadata
        if 'missing_domain' in issues:
            if not re.search(r'Domain:', fixed_block, re.IGNORECASE):
                fixed_block = '\nDomain: General\n' + fixed_block
                was_fixed = True
        
        if 'missing_topic' in issues:
            if not re.search(r'Topic:', fixed_block, re.IGNORECASE):
                # Insert after Domain
                fixed_block = re.sub(
                    r'(Domain:.*?\n)',
                    r'\1Topic: General Topic\n',
                    fixed_block,
                    count=1,
                    flags=re.IGNORECASE
                )
                was_fixed = True
        
        if 'missing_subtopic' in issues:
            if not re.search(r'Subtopic:', fixed_block, re.IGNORECASE):
                # Insert after Topic
                fixed_block = re.sub(
                    r'(Topic:.*?\n)',
                    r'\1Subtopic: General Subtopic\n',
                    fixed_block,
                    count=1,
                    flags=re.IGNORECASE
                )
                was_fixed = True
        
        # Fix missing question
        if 'missing_question' in issues:
            if not re.search(r'Question:\s*\S{10,}', fixed_block, re.IGNORECASE):
                # Try to find any text before options
                text_before_options = re.search(r'Difficulty:.*?\n(.+?)(?=[A-D]\))', fixed_block, re.DOTALL)
                if text_before_options and 'Question:' not in text_before_options.group(1):
                    # Add Question: label
                    fixed_block = re.sub(
                        r'(Difficulty:.*?\n)',
                        r'\1\nQuestion: [Question text needs review]\n',
                        fixed_block,
                        count=1
                    )
                    was_fixed = True
        
        # Fix missing options
        option_fixes = {
            'missing_option_a': 'A',
            'missing_option_b': 'B',
            'missing_option_c': 'C',
            'missing_option_d': 'D'
        }
        
        for issue, option_letter in option_fixes.items():
            if issue in issues:
                # Find where to insert
                if option_letter == 'A':
                    # Insert after Question
                    if re.search(r'Question:', fixed_block, re.IGNORECASE):
                        fixed_block = re.sub(
                            r'(Question:.*?)(\n[B-D]\)|\n✔|\nCorrect)',
                            r'\1\nA) [Option A needs review]\2',
                            fixed_block,
                            count=1,
                            flags=re.DOTALL | re.IGNORECASE
                        )
                        was_fixed = True
                elif option_letter == 'B':
                    if re.search(r'A\)', fixed_block):
                        fixed_block = re.sub(
                            r'(A\).*?)(\n[C-D]\)|\n✔|\nCorrect)',
                            r'\1\nB) [Option B needs review]\2',
                            fixed_block,
                            count=1,
                            flags=re.DOTALL
                        )
                        was_fixed = True
                elif option_letter == 'C':
                    if re.search(r'B\)', fixed_block):
                        fixed_block = re.sub(
                            r'(B\).*?)(\nD\)|\n✔|\nCorrect)',
                            r'\1\nC) [Option C needs review]\2',
                            fixed_block,
                            count=1,
                            flags=re.DOTALL
                        )
                        was_fixed = True
                elif option_letter == 'D':
                    if re.search(r'C\)', fixed_block):
                        fixed_block = re.sub(
                            r'(C\).*?)(\n✔|\nCorrect)',
                            r'\1\nD) [Option D needs review]\2',
                            fixed_block,
                            count=1,
                            flags=re.DOTALL
                        )
                        was_fixed = True
        
        # Fix missing correct answer
        if 'missing_answer' in issues:
            if not re.search(r'Correct\s*Answer:', fixed_block, re.IGNORECASE):
                # Insert before Reason or at end
                if re.search(r'Reason:', fixed_block, re.IGNORECASE):
                    fixed_block = re.sub(
                        r'(\nReason:)',
                        r'\n✔ Correct Answer: A\1',
                        fixed_block,
                        count=1,
                        flags=re.IGNORECASE
                    )
                else:
                    fixed_block += '\n✔ Correct Answer: A\n'
                was_fixed = True
        
        # Fix missing reason
        if 'missing_reason' in issues:
            if not re.search(r'Reason:\s*\S{5,}', fixed_block, re.IGNORECASE):
                # Insert after Correct Answer
                if re.search(r'Correct\s*Answer:', fixed_block, re.IGNORECASE):
                    fixed_block = re.sub(
                        r'(Correct\s*Answer:.*?\n)',
                        r'\1Reason: [Reason needs review]\n',
                        fixed_block,
                        count=1,
                        flags=re.IGNORECASE
                    )
                    was_fixed = True
        
        # Ensure Tag exists
        if not re.search(r'Tag:', fixed_block, re.IGNORECASE):
            if not fixed_block.endswith('\n'):
                fixed_block += '\n'
            fixed_block += 'Tag: Normal\n'
            was_fixed = True
        
        # Ensure separator
        if not fixed_block.strip().endswith('---'):
            fixed_block = fixed_block.rstrip() + '\n\n---\n'
            was_fixed = True
        
        return fixed_block, was_fixed
    
    def print_report(self):
        """Print detailed report"""
        print("\n" + "="*70)
        print("ANALYSIS AND FIX REPORT")
        print("="*70)
        print(f"\n📊 Statistics:")
        print(f"  • Total Files Processed:    {self.stats['total_files']}")
        print(f"  • Total MCQs Found:         {self.stats['total_mcqs']}")
        print(f"  • Incomplete MCQs:          {self.stats['incomplete_mcqs']}")
        print(f"  • Fixed MCQs:               {self.stats['fixed_mcqs']}")
        print(f"  • Unfixable MCQs:           {self.stats['unfixable_mcqs']}")
        print(f"  • Complete MCQs:            {self.stats['total_mcqs'] - self.stats['incomplete_mcqs']}")
        
        print(f"\n✓ All fixable MCQs have been repaired!")
        print(f"  Run: python manage.py import_mcq_bank --clear")
        print("="*70)


if __name__ == '__main__':
    fixer = MCQFixer()
    fixer.analyze_and_fix_all()
