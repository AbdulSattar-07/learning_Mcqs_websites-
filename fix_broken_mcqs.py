#!/usr/bin/env python
"""
Script to automatically fix broken MCQs by analyzing patterns and fixing formatting
"""

import os
import re
from pathlib import Path

def read_file(filepath):
    """Read file content"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """Write content to file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def fix_missing_option(content, q_num, option_letter):
    """Fix missing option by looking at the pattern"""
    # Find the question block
    pattern = f'###\\s+Question\\s+{q_num}\\b(.*?)(?=###\\s+Question\\s+\\d+|\\Z)'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        return content
    
    block = match.group(1)
    block_start = match.start(1)
    
    # Determine what comes after the missing option
    if option_letter == 'A':
        # A is missing, look for B
        next_pattern = r'\nB\)'
    elif option_letter == 'B':
        # B is missing, look for C
        next_pattern = r'\nC\)'
    elif option_letter == 'C':
        # C is missing, look for D
        next_pattern = r'\nD\)'
    elif option_letter == 'D':
        # D is missing, look for correct answer
        next_pattern = r'\n✔'
    else:
        return content
    
    next_match = re.search(next_pattern, block)
    if not next_match:
        return content
    
    # Find where to insert the missing option
    insert_pos = block_start + next_match.start()
    
    # Create the missing option line
    missing_option = f"\n{option_letter}) [Missing option - Please review]\n"
    
    # Insert it
    new_content = content[:insert_pos] + missing_option + content[insert_pos:]
    
    return new_content

def fix_missing_question(content, q_num):
    """Fix missing question text"""
    pattern = f'###\\s+Question\\s+{q_num}\\b(.*?)(?=###\\s+Question\\s+\\d+|\\Z)'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        return content
    
    block = match.group(1)
    block_start = match.start(1)
    
    # Check if Question: line exists
    if not re.search(r'\nQuestion:', block):
        # Find where to insert (after Difficulty line)
        diff_match = re.search(r'Difficulty:.*?\n', block)
        if diff_match:
            insert_pos = block_start + diff_match.end()
            missing_q = "\nQuestion: [Missing question - Please review]\n"
            new_content = content[:insert_pos] + missing_q + content[insert_pos:]
            return new_content
    
    return content

def fix_missing_subtopic(content, q_num):
    """Fix missing subtopic"""
    pattern = f'###\\s+Question\\s+{q_num}\\b(.*?)(?=###\\s+Question\\s+\\d+|\\Z)'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        return content
    
    block = match.group(1)
    block_start = match.start(1)
    
    # Check if Subtopic: line exists
    if not re.search(r'\nSubtopic:', block):
        # Find where to insert (after Topic line)
        topic_match = re.search(r'Topic:.*?\n', block)
        if topic_match:
            insert_pos = block_start + topic_match.end()
            missing_st = "Subtopic: General\n"
            new_content = content[:insert_pos] + missing_st + content[insert_pos:]
            return new_content
    
    return content

def process_file(filepath, broken_mcqs):
    """Process a single file and fix all broken MCQs"""
    print(f"\n📝 Fixing: {filepath}")
    
    content = read_file(filepath)
    original_content = content
    fixes_made = 0
    
    for mcq in broken_mcqs:
        q_num = mcq['question_num']
        missing = mcq['missing']
        
        # Fix missing fields
        if 'subtopic' in missing:
            content = fix_missing_subtopic(content, q_num)
            fixes_made += 1
        
        if 'question' in missing:
            content = fix_missing_question(content, q_num)
            fixes_made += 1
        
        for option in ['option_a', 'option_b', 'option_c', 'option_d']:
            if option in missing:
                letter = option.split('_')[1].upper()
                content = fix_missing_option(content, q_num, letter)
                fixes_made += 1
    
    # Only write if changes were made
    if content != original_content:
        write_file(filepath, content)
        print(f"   ✓ Fixed {fixes_made} issues in {len(broken_mcqs)} MCQs")
        return fixes_made
    else:
        print(f"   ⚠ No automatic fixes possible")
        return 0

def main():
    """Main function to fix all broken MCQs"""
    print("="*70)
    print("AUTOMATED MCQ FIXER")
    print("="*70)
    
    # Read the broken MCQs report
    if not os.path.exists('broken_mcqs_report.txt'):
        print("Error: broken_mcqs_report.txt not found!")
        print("Please run find_broken_mcqs.py first")
        return
    
    # Parse the report
    with open('broken_mcqs_report.txt', 'r', encoding='utf-8') as f:
        report = f.read()
    
    # Extract file paths and broken MCQs
    file_sections = re.split(r'={70}\nFILE: (.+?)\n', report)[1:]
    
    total_fixes = 0
    files_processed = 0
    
    # Process each file
    for i in range(0, len(file_sections), 2):
        filepath = file_sections[i].strip()
        section_content = file_sections[i + 1]
        
        # Extract broken MCQs for this file
        broken_mcqs = []
        mcq_blocks = re.findall(
            r'Question (\d+)\nMissing: ([^\n]+)',
            section_content
        )
        
        for q_num, missing_str in mcq_blocks:
            missing = [m.strip() for m in missing_str.split(',')]
            broken_mcqs.append({
                'question_num': q_num,
                'missing': missing
            })
        
        if broken_mcqs:
            fixes = process_file(filepath, broken_mcqs)
            total_fixes += fixes
            files_processed += 1
    
    print(f"\n{'='*70}")
    print(f"SUMMARY")
    print(f"{'='*70}")
    print(f"Files processed: {files_processed}")
    print(f"Total fixes made: {total_fixes}")
    print(f"\n✓ Automatic fixes completed!")
    print(f"\nNote: Some MCQs may need manual review.")
    print(f"Look for '[Missing option - Please review]' markers.")

if __name__ == '__main__':
    main()
