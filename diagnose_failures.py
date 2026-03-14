#!/usr/bin/env python
"""
Diagnose exactly which MCQs are failing and why
"""

import os
import re

def parse_single_mcq(block, q_num):
    """Parse a single MCQ and return issues"""
    issues = []
    mcq_data = {}
    
    # Extract Domain
    domain_match = re.search(r'Domain:\s*(.+?)(?=\n)', block, re.IGNORECASE)
    if domain_match:
        mcq_data['domain'] = domain_match.group(1).strip()
    else:
        issues.append('missing_domain')
    
    # Extract Topic
    topic_match = re.search(r'Topic:\s*(.+?)(?=\n)', block, re.IGNORECASE)
    if topic_match:
        mcq_data['topic'] = topic_match.group(1).strip()
    else:
        issues.append('missing_topic')
    
    # Extract Subtopic
    subtopic_match = re.search(r'Subtopic:\s*(.+?)(?=\n)', block, re.IGNORECASE)
    if subtopic_match:
        mcq_data['subtopic'] = subtopic_match.group(1).strip()
    else:
        issues.append('missing_subtopic')
    
    # Extract Question
    question_match = re.search(r'Question:\s*(.+?)(?=\n[A-D]\))', block, re.DOTALL | re.IGNORECASE)
    if question_match:
        mcq_data['question'] = question_match.group(1).strip()
    else:
        issues.append('missing_question')
    
    # Extract Options
    option_a_match = re.search(r'A\)\s*(.+?)(?=\n[B-D]\)|\n✔|\nCorrect)', block, re.DOTALL | re.IGNORECASE)
    if option_a_match:
        mcq_data['option_a'] = option_a_match.group(1).strip()
    else:
        issues.append('missing_option_a')
    
    option_b_match = re.search(r'B\)\s*(.+?)(?=\n[C-D]\)|\n✔|\nCorrect)', block, re.DOTALL | re.IGNORECASE)
    if option_b_match:
        mcq_data['option_b'] = option_b_match.group(1).strip()
    else:
        issues.append('missing_option_b')
    
    option_c_match = re.search(r'C\)\s*(.+?)(?=\nD\)|\n✔|\nCorrect)', block, re.DOTALL | re.IGNORECASE)
    if option_c_match:
        mcq_data['option_c'] = option_c_match.group(1).strip()
    else:
        issues.append('missing_option_c')
    
    option_d_match = re.search(r'D\)\s*(.+?)(?=\n✔|\nCorrect)', block, re.DOTALL | re.IGNORECASE)
    if option_d_match:
        mcq_data['option_d'] = option_d_match.group(1).strip()
    else:
        issues.append('missing_option_d')
    
    # Extract Correct Answer
    answer_match = re.search(r'(?:✔\s*)?Correct\s*Answer:\s*([A-D])', block, re.IGNORECASE)
    if answer_match:
        mcq_data['correct_answer'] = answer_match.group(1).strip().upper()
    else:
        issues.append('missing_answer')
    
    # Extract Reason
    reason_match = re.search(r'Reason:\s*(.+?)(?=\nTag:|\n---|\Z)', block, re.DOTALL | re.IGNORECASE)
    if reason_match:
        mcq_data['reason'] = reason_match.group(1).strip()
    else:
        issues.append('missing_reason')
    
    return issues, mcq_data

def diagnose_file(filepath):
    """Diagnose a single file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by questions
    question_blocks = re.split(r'###\s+Question\s+(\d+)', content)
    
    failures = []
    
    for i in range(1, len(question_blocks), 2):
        if i + 1 >= len(question_blocks):
            break
        
        q_num = question_blocks[i]
        block = question_blocks[i + 1]
        
        issues, mcq_data = parse_single_mcq(block, q_num)
        
        if issues:
            failures.append({
                'q_num': q_num,
                'issues': issues,
                'preview': block[:200]
            })
    
    return failures

# Diagnose the problematic files
problematic_files = [
    'MCQ_BANK/Domain_04_Operating_Systems/os_mcq_batch_10.md',  # 59/100
    'MCQ_BANK/Domain_05_Software_Engineering/se_mcq_batch_06.md',  # 44/50
    'MCQ_BANK/Domain_07_AI_ML_Data_Analytics/aiml_mcq_batch_09.md',  # 71/100
    'MCQ_BANK/Domain_08_Cyber_Security/cybersecurity_mcq_batch_09.md',  # 68/100
]

print("="*70)
print("DIAGNOSING FAILED MCQs")
print("="*70)

for filepath in problematic_files:
    if not os.path.exists(filepath):
        continue
    
    print(f"\n📁 {filepath}")
    failures = diagnose_file(filepath)
    
    print(f"   Failed: {len(failures)} MCQs")
    
    # Show first 3 failures
    for fail in failures[:3]:
        print(f"\n   Q{fail['q_num']}: {', '.join(fail['issues'])}")
        print(f"   Preview: {fail['preview'][:150]}...")

print("\n" + "="*70)
