#!/usr/bin/env python
"""
Find the exact MCQs that are failing import validation
"""

import os
import re
from pathlib import Path

def parse_single_mcq(block, batch_filename):
    """Parse a single MCQ - same logic as import script"""
    mcq_data = {}
    
    # Extract Domain
    domain_match = re.search(r'Domain:\s*(.+?)(?=\n)', block, re.IGNORECASE)
    if domain_match:
        mcq_data['domain'] = domain_match.group(1).strip()
    
    # Extract Topic
    topic_match = re.search(r'Topic:\s*(.+?)(?=\n)', block, re.IGNORECASE)
    if topic_match:
        mcq_data['topic'] = topic_match.group(1).strip()
    
    # Extract Subtopic
    subtopic_match = re.search(r'Subtopic:\s*(.+?)(?=\n)', block, re.IGNORECASE)
    if subtopic_match:
        mcq_data['subtopic'] = subtopic_match.group(1).strip()
    
    # Extract Difficulty
    difficulty_match = re.search(r'Difficulty:\s*(.+?)(?=\n)', block, re.IGNORECASE)
    if difficulty_match:
        mcq_data['difficulty'] = difficulty_match.group(1).strip()
    
    # Extract Question - improved pattern
    question_match = re.search(r'Question:\s*(.+?)(?=\n[A-D]\))', block, re.DOTALL | re.IGNORECASE)
    if question_match:
        mcq_data['question'] = question_match.group(1).strip()
    
    # Extract Options - improved patterns to handle multiline
    option_a_match = re.search(r'A\)\s*(.+?)(?=\n[B-D]\)|\n✔|\nCorrect)', block, re.DOTALL | re.IGNORECASE)
    if option_a_match:
        mcq_data['option_a'] = option_a_match.group(1).strip()
    
    option_b_match = re.search(r'B\)\s*(.+?)(?=\n[C-D]\)|\n✔|\nCorrect)', block, re.DOTALL | re.IGNORECASE)
    if option_b_match:
        mcq_data['option_b'] = option_b_match.group(1).strip()
    
    option_c_match = re.search(r'C\)\s*(.+?)(?=\nD\)|\n✔|\nCorrect)', block, re.DOTALL | re.IGNORECASE)
    if option_c_match:
        mcq_data['option_c'] = option_c_match.group(1).strip()
    
    option_d_match = re.search(r'D\)\s*(.+?)(?=\n✔|\nCorrect)', block, re.DOTALL | re.IGNORECASE)
    if option_d_match:
        mcq_data['option_d'] = option_d_match.group(1).strip()
    
    # Extract Correct Answer - multiple patterns
    answer_match = re.search(r'(?:✔\s*)?Correct\s*Answer:\s*([A-D])', block, re.IGNORECASE)
    if answer_match:
        mcq_data['correct_answer'] = answer_match.group(1).strip().upper()
    
    # Extract Reason - improved pattern
    reason_match = re.search(r'Reason:\s*(.+?)(?=\nTag:|\n---|\Z)', block, re.DOTALL | re.IGNORECASE)
    if reason_match:
        mcq_data['reason'] = reason_match.group(1).strip()
    
    # Extract Tag
    tag_match = re.search(r'Tag:\s*(.+?)(?=\n---|\Z)', block, re.IGNORECASE)
    if tag_match:
        mcq_data['tag'] = tag_match.group(1).strip()
    else:
        mcq_data['tag'] = 'Normal'  # Default tag
    
    # Add batch filename
    mcq_data['batch_name'] = batch_filename.replace('.md', '')
    
    # Validate required fields
    required_fields = ['domain', 'topic', 'subtopic', 'question', 
                      'option_a', 'option_b', 'option_c', 'option_d', 
                      'correct_answer', 'reason']
    
    missing = [f for f in required_fields if f not in mcq_data or not mcq_data[f]]
    
    if missing:
        return None, missing
    
    return mcq_data, []

def analyze_file(filepath, batch_filename):
    """Analyze a file and return failures"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by questions
    question_blocks = re.split(r'###\s+Question\s+(\d+)', content)
    
    failures = []
    successes = 0
    
    for i in range(1, len(question_blocks), 2):
        if i + 1 >= len(question_blocks):
            break
        
        q_num = question_blocks[i]
        block = question_blocks[i + 1]
        
        mcq_data, missing = parse_single_mcq(block, batch_filename)
        
        if missing:
            failures.append({
                'q_num': q_num,
                'missing': missing,
                'block': block
            })
        else:
            successes += 1
    
    return failures, successes

# Analyze all files
print("="*70)
print("FINDING EXACT FAILURES")
print("="*70)

mcq_bank_path = 'MCQ_BANK'
total_failures = 0
total_successes = 0
files_with_failures = []

for domain_folder in sorted(os.listdir(mcq_bank_path)):
    domain_path = os.path.join(mcq_bank_path, domain_folder)
    
    if not os.path.isdir(domain_path) or not domain_folder.startswith('Domain_'):
        continue
    
    for batch_file in sorted(os.listdir(domain_path)):
        if not batch_file.endswith('.md'):
            continue
        
        batch_path = os.path.join(domain_path, batch_file)
        failures, successes = analyze_file(batch_path, batch_file)
        
        total_failures += len(failures)
        total_successes += successes
        
        if failures:
            files_with_failures.append({
                'file': f"{domain_folder}/{batch_file}",
                'failures': failures
            })

print(f"\nTotal Successes: {total_successes}")
print(f"Total Failures: {total_failures}")
print(f"\nFiles with failures: {len(files_with_failures)}")

# Show details of first few failures
print("\n" + "="*70)
print("FAILURE DETAILS (First 10)")
print("="*70)

count = 0
for file_info in files_with_failures:
    if count >= 10:
        break
    
    print(f"\n📁 {file_info['file']}")
    for fail in file_info['failures'][:2]:  # Show first 2 from each file
        if count >= 10:
            break
        count += 1
        
        print(f"\n  Q{fail['q_num']}: Missing {', '.join(fail['missing'])}")
        print(f"  Block preview:")
        print(f"  {fail['block'][:300]}...")

print("\n" + "="*70)
