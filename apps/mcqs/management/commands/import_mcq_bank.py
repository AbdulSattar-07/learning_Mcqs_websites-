import os
import re
from pathlib import Path
from django.core.management.base import BaseCommand
from django.db import transaction
from apps.mcqs.models import Domain, Topic, Subtopic, Batch, MCQ


class Command(BaseCommand):
    help = 'Import entire MCQ_BANK dataset into database'
    
    def __init__(self):
        super().__init__()
        self.stats = {
            'domains': 0,
            'topics': 0,
            'subtopics': 0,
            'batches': 0,
            'mcqs': 0,
            'skipped': 0,
            'errors': 0
        }
        self.verbosity = 1
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--path',
            type=str,
            default='MCQ_BANK',
            help='Path to MCQ_BANK folder (default: MCQ_BANK)'
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing MCQs before import'
        )
    
    def handle(self, *args, **options):
        mcq_bank_path = options['path']
        clear_existing = options['clear']
        self.verbosity = options.get('verbosity', 1)
        
        # Validate path
        if not os.path.exists(mcq_bank_path):
            self.stdout.write(self.style.ERROR(f'Path not found: {mcq_bank_path}'))
            return
        
        # Clear existing data if requested
        if clear_existing:
            self.stdout.write(self.style.WARNING('Clearing existing MCQs...'))
            MCQ.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Cleared existing MCQs'))
        
        # Start import
        self.stdout.write(self.style.SUCCESS('=' * 70))
        self.stdout.write(self.style.SUCCESS('Starting MCQ Bank Import'))
        self.stdout.write(self.style.SUCCESS('=' * 70))
        
        # Process all domain folders
        self.process_mcq_bank(mcq_bank_path)
        
        # Print final statistics
        self.print_statistics()
    
    def process_mcq_bank(self, base_path):
        """Process all domain folders in MCQ_BANK"""
        domain_folders = sorted([
            d for d in os.listdir(base_path)
            if os.path.isdir(os.path.join(base_path, d)) and d.startswith('Domain_')
        ])
        
        for domain_folder in domain_folders:
            domain_path = os.path.join(base_path, domain_folder)
            self.process_domain_folder(domain_path, domain_folder)
    
    def process_domain_folder(self, domain_path, domain_folder_name):
        """Process a single domain folder"""
        # Extract domain name from folder
        domain_name = self.extract_domain_name(domain_folder_name)
        
        self.stdout.write(self.style.SUCCESS(f'\n📁 Processing Domain: {domain_name}'))
        self.stdout.write(self.style.SUCCESS('-' * 70))
        
        # Get all batch files
        batch_files = sorted([
            f for f in os.listdir(domain_path)
            if f.endswith('.md') and 'batch' in f.lower()
        ])
        
        if not batch_files:
            self.stdout.write(self.style.WARNING(f'  No batch files found in {domain_folder_name}'))
            return
        
        # Process each batch file
        for batch_file in batch_files:
            batch_path = os.path.join(domain_path, batch_file)
            self.process_batch_file(batch_path, batch_file)
    
    def process_batch_file(self, batch_path, batch_filename):
        """Process a single batch file"""
        self.stdout.write(f'  📄 Reading: {batch_filename}')
        
        try:
            with open(batch_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Parse MCQs from file
            mcqs = self.parse_mcqs(content, batch_filename)
            
            # Import MCQs
            imported = self.import_mcqs(mcqs)
            
            total_parsed = len(mcqs)
            
            if imported == total_parsed and total_parsed > 0:
                self.stdout.write(self.style.SUCCESS(
                    f'     ✓ Imported: {imported}/{total_parsed} MCQs'
                ))
            elif imported > 0:
                self.stdout.write(self.style.WARNING(
                    f'     ⚠ Imported: {imported}/{total_parsed} MCQs'
                ))
            else:
                self.stdout.write(self.style.ERROR(
                    f'     ✗ Failed: 0/{total_parsed} MCQs imported'
                ))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'     ✗ Error: {str(e)}'))
            self.stats['errors'] += 1
    
    def parse_mcqs(self, content, batch_filename):
        """Parse MCQs from markdown content"""
        mcqs = []
        
        # Split content by question markers
        question_blocks = re.split(r'###\s+Question\s+\d+', content)
        
        total_questions = len(question_blocks) - 1
        
        for idx, block in enumerate(question_blocks[1:], 1):  # Skip first empty split
            try:
                mcq_data = self.parse_single_mcq(block, batch_filename)
                if mcq_data:
                    mcqs.append(mcq_data)
            except Exception as e:
                self.stdout.write(self.style.WARNING(
                    f'     ⚠ Q{idx}/{total_questions}: {str(e)[:80]}'
                ))
                self.stats['errors'] += 1
                
                # Debug: Show first 200 chars of problematic block
                if self.verbosity >= 2:
                    self.stdout.write(f'     Block preview: {block[:200]}...')
        
        return mcqs
    
    def parse_single_mcq(self, block, batch_filename):
        """Parse a single MCQ from text block with improved regex"""
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
            # Try to provide more context for debugging
            raise ValueError(f"Missing fields: {', '.join(missing)}")
        
        return mcq_data
    
    @transaction.atomic
    def import_mcqs(self, mcqs):
        """Import parsed MCQs into database"""
        imported_count = 0
        
        for mcq_data in mcqs:
            try:
                # Get or create Domain
                domain, created = Domain.objects.get_or_create(
                    name=mcq_data['domain']
                )
                if created:
                    self.stats['domains'] += 1
                
                # Get or create Topic
                topic, created = Topic.objects.get_or_create(
                    domain=domain,
                    name=mcq_data['topic']
                )
                if created:
                    self.stats['topics'] += 1
                
                # Get or create Subtopic
                subtopic, created = Subtopic.objects.get_or_create(
                    topic=topic,
                    name=mcq_data['subtopic']
                )
                if created:
                    self.stats['subtopics'] += 1
                
                # Get or create Batch
                batch, created = Batch.objects.get_or_create(
                    name=mcq_data['batch_name']
                )
                if created:
                    self.stats['batches'] += 1
                
                # Check for duplicate MCQ
                existing = MCQ.objects.filter(
                    domain=domain,
                    topic=topic,
                    subtopic=subtopic,
                    question_text=mcq_data['question']
                ).exists()
                
                if existing:
                    self.stats['skipped'] += 1
                    continue
                
                # Create MCQ
                MCQ.objects.create(
                    domain=domain,
                    topic=topic,
                    subtopic=subtopic,
                    batch=batch,
                    difficulty=mcq_data.get('difficulty', 'Medium'),
                    tag=mcq_data.get('tag', ''),
                    question_text=mcq_data['question'],
                    option_a=mcq_data['option_a'],
                    option_b=mcq_data['option_b'],
                    option_c=mcq_data['option_c'],
                    option_d=mcq_data['option_d'],
                    correct_answer=mcq_data['correct_answer'],
                    reason=mcq_data['reason']
                )
                
                self.stats['mcqs'] += 1
                imported_count += 1
                
            except Exception as e:
                self.stdout.write(self.style.WARNING(
                    f'     Warning: Failed to import MCQ - {str(e)}'
                ))
                self.stats['errors'] += 1
        
        return imported_count
    
    def extract_domain_name(self, folder_name):
        """Extract clean domain name from folder name"""
        # Remove Domain_XX_ prefix
        name = re.sub(r'^Domain_\d+_', '', folder_name)
        # Replace underscores with spaces
        name = name.replace('_', ' ')
        return name
    
    def print_statistics(self):
        """Print import statistics"""
        self.stdout.write(self.style.SUCCESS('\n' + '=' * 70))
        self.stdout.write(self.style.SUCCESS('Import Complete!'))
        self.stdout.write(self.style.SUCCESS('=' * 70))
        self.stdout.write(f'\n📊 Statistics:')
        self.stdout.write(f'  • Domains Created:   {self.stats["domains"]}')
        self.stdout.write(f'  • Topics Created:    {self.stats["topics"]}')
        self.stdout.write(f'  • Subtopics Created: {self.stats["subtopics"]}')
        self.stdout.write(f'  • Batches Created:   {self.stats["batches"]}')
        self.stdout.write(self.style.SUCCESS(f'  • MCQs Imported:     {self.stats["mcqs"]}'))
        self.stdout.write(self.style.WARNING(f'  • MCQs Skipped:      {self.stats["skipped"]}'))
        if self.stats['errors'] > 0:
            self.stdout.write(self.style.ERROR(f'  • Errors:            {self.stats["errors"]}'))
        self.stdout.write(self.style.SUCCESS('\n✓ All MCQs have been imported successfully!'))
        self.stdout.write(self.style.SUCCESS('=' * 70 + '\n'))
