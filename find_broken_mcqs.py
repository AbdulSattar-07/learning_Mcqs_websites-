#!/usr/bin/env python
"""
Script to find and log all broken MCQs that failed to parse
"""

import os
import re

def find_broken_mcqs():
    """Find all MCQs with formatting issues"""
    
    broken_mcqs = []
    mcq_bank_path = 'MCQ_BANK'
    
    # Get all domain folders
    domain_folders = sorted([
        d for d in os.listdir(mcq_bank_path)
        if os.path.isdir(os.path.join(mcq_bank_path, d)) and d.startswith('Domain_')
    ])
    
    for domain_folder in domain_folders:
        domain_path = os.path.join(mcq_bank_path, domain_folder)
        
        # Get all batch files
        batch_files = sorted([
            f for f in os.listdir(domain_path)
            if f.endswith('.md') and 'batch' in f.lower()
        ])
        
        for batch_file in batch_files:
            batch_path = os.path.join(domain_path, batch_file)
            
            with open(batch_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Split by questions
            question_blocks = re.split(r'###\s+Question\s+(\d+)', content)
            
            # Process each question
            for i in range(1, len(question_blocks), 2):
                q_num = question_blocks[i]
                block = question_blocks[i + 1] if i + 1 < len(question_blocks) else ""
                
                # Check for required fields
                has_domain = bool(re.search(r'Domain:\s*(.+?)(?=\n)', block, re.IGNORECASE))
                has_topic = bool(re.search(r'Topic:\s*(.+?)(?=\n)', block, re.IGNORECASE))
                has_subtopic = bool(re.search(r'Subtopic:\s*(.+?)(?=\n)', block, re.IGNORECASE))
                has_question = bool(re.search(r'Question:\s*(.+?)(?=\n[A-D]\))', block, re.DOTALL | re.IGNORECASE))
                has_option_a = bool(re.search(r'A\)\s*(.+?)(?=\n[B-D]\)|\n✔|\nCorrect)', block, re.DOTALL | re.IGNORECASE))
                has_option_b = bool(re.search(r'B\)\s*(.+?)(?=\n[C-D]\)|\n✔|\nCorrect)', block, re.DOTALL | re.IGNORECASE))
                has_option_c = bool(re.search(r'C\)\s*(.+?)(?=\nD\)|\n✔|\nCorrect)', block, re.DOTALL | re.IGNORECASE))
                has_option_d = bool(re.search(r'D\)\s*(.+?)(?=\n✔|\nCorrect)', block, re.DOTALL | re.IGNORECASE))
                has_answer = bool(re.search(r'(?:✔\s*)?Correct\s*Answer:\s*([A-D])', block, re.IGNORECASE))
                has_reason = bool(re.search(r'Reason:\s*(.+?)(?=\nTag:|\n---|\Z)', block, re.DOTALL | re.IGNORECASE))
                
                missing = []
                if not has_domain: missing.append('domain')
                if not has_topic: missing.append('topic')
                if not has_subtopic: missing.append('subtopic')
                if not has_question: missing.append('question')
                if not has_option_a: missing.append('option_a')
                if not has_option_b: missing.append('option_b')
                if not has_option_c: missing.append('option_c')
                if not has_option_d: missing.append('option_d')
                if not has_answer: missing.append('answer')
                if not has_reason: missing.append('reason')
                
                if missing:
                    broken_mcqs.append({
                        'file': batch_path,
                        'question_num': q_num,
                        'missing': missing,
                        'block_preview': block[:300]
                    })
    
    return broken_mcqs


if __name__ == '__main__':
    print("Finding broken MCQs...")
    broken = find_broken_mcqs()
    
    print(f"\n{'='*70}")
    print(f"Found {len(broken)} broken MCQs")
    print(f"{'='*70}\n")
    
    # Group by file
    by_file = {}
    for mcq in broken:
        file = mcq['file']
        if file not in by_file:
            by_file[file] = []
        by_file[file].append(mcq)
    
    # Print summary
    for file, mcqs in sorted(by_file.items()):
        print(f"\n📁 {file}")
        print(f"   Broken MCQs: {len(mcqs)}")
        for mcq in mcqs[:5]:  # Show first 5
            print(f"   - Q{mcq['question_num']}: Missing {', '.join(mcq['missing'])}")
        if len(mcqs) > 5:
            print(f"   ... and {len(mcqs) - 5} more")
    
    # Save detailed report
    with open('broken_mcqs_report.txt', 'w', encoding='utf-8') as f:
        f.write(f"BROKEN MCQs REPORT\n")
        f.write(f"{'='*70}\n")
        f.write(f"Total: {len(broken)} broken MCQs\n\n")
        
        for file, mcqs in sorted(by_file.items()):
            f.write(f"\n{'='*70}\n")
            f.write(f"FILE: {file}\n")
            f.write(f"Broken MCQs: {len(mcqs)}\n")
            f.write(f"{'='*70}\n\n")
            
            for mcq in mcqs:
                f.write(f"Question {mcq['question_num']}\n")
                f.write(f"Missing: {', '.join(mcq['missing'])}\n")
                f.write(f"Preview:\n{mcq['block_preview']}\n")
                f.write(f"{'-'*70}\n\n")
    
    print(f"\n✓ Detailed report saved to: broken_mcqs_report.txt")
