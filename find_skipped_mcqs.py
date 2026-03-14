#!/usr/bin/env python
"""
Find all skipped/duplicate MCQs to understand what's missing
"""

import os
import re
from collections import defaultdict

def analyze_file(filepath):
    """Analyze a file for duplicate questions"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by questions
    question_blocks = re.split(r'###\s+Question\s+(\d+)', content)
    
    questions = []
    for i in range(1, len(question_blocks), 2):
        if i + 1 >= len(question_blocks):
            break
            
        q_num = question_blocks[i]
        block = question_blocks[i + 1]
        
        # Extract question text
        q_match = re.search(r'Question:\s*(.+?)(?=\n[A-D]\)|\n✔|\Z)', block, re.DOTALL | re.IGNORECASE)
        if q_match:
            q_text = q_match.group(1).strip()[:100]  # First 100 chars
            questions.append({
                'num': q_num,
                'text': q_text,
                'block': block[:200]
            })
    
    # Find duplicates
    seen = {}
    duplicates = []
    
    for q in questions:
        if q['text'] in seen:
            duplicates.append({
                'file': filepath,
                'q1': seen[q['text']],
                'q2': q['num'],
                'text': q['text']
            })
        else:
            seen[q['text']] = q['num']
    
    return duplicates, len(questions)

def main():
    print("="*70)
    print("FINDING SKIPPED/DUPLICATE MCQs")
    print("="*70)
    
    mcq_bank_path = 'MCQ_BANK'
    all_duplicates = []
    total_mcqs = 0
    
    # Process all files
    for root, dirs, files in os.walk(mcq_bank_path):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                duplicates, count = analyze_file(filepath)
                total_mcqs += count
                
                if duplicates:
                    all_duplicates.extend(duplicates)
                    print(f"\n📁 {filepath}")
                    print(f"   Found {len(duplicates)} duplicate(s)")
                    for dup in duplicates:
                        print(f"   - Q{dup['q1']} = Q{dup['q2']}: {dup['text'][:50]}...")
    
    print(f"\n{'='*70}")
    print(f"SUMMARY")
    print(f"{'='*70}")
    print(f"Total MCQs found: {total_mcqs}")
    print(f"Total duplicates: {len(all_duplicates)}")
    print(f"Expected unique: {total_mcqs - len(all_duplicates)}")
    print(f"Actual imported: 9596")
    print(f"Skipped: 357")
    print(f"Difference: {total_mcqs - len(all_duplicates) - 9596}")

if __name__ == '__main__':
    main()
