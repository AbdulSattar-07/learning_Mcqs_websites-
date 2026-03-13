import csv
import json
from django.core.management.base import BaseCommand
from apps.mcqs.models import Domain, Topic, Subtopic, Batch, MCQ


class Command(BaseCommand):
    help = 'Import MCQs from CSV or JSON file'
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to CSV or JSON file')
        parser.add_argument('--format', type=str, default='csv', choices=['csv', 'json'], help='File format')
    
    def handle(self, *args, **options):
        file_path = options['file_path']
        file_format = options['format']
        
        if file_format == 'csv':
            self.import_from_csv(file_path)
        else:
            self.import_from_json(file_path)
    
    def import_from_csv(self, file_path):
        """Import MCQs from CSV file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                count = 0
                
                for row in reader:
                    try:
                        domain, _ = Domain.objects.get_or_create(name=row['domain'])
                        topic, _ = Topic.objects.get_or_create(domain=domain, name=row['topic'])
                        subtopic, _ = Subtopic.objects.get_or_create(topic=topic, name=row['subtopic'])
                        
                        batch = None
                        if row.get('batch'):
                            batch, _ = Batch.objects.get_or_create(name=row['batch'])

                        MCQ.objects.create(
                            domain=domain,
                            topic=topic,
                            subtopic=subtopic,
                            batch=batch,
                            difficulty=row.get('difficulty', 'Medium'),
                            tag=row.get('tag', ''),
                            question_text=row['question_text'],
                            option_a=row['option_a'],
                            option_b=row['option_b'],
                            option_c=row['option_c'],
                            option_d=row['option_d'],
                            correct_answer=row['correct_answer'].upper(),
                            reason=row['reason']
                        )
                        count += 1
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Error importing row: {e}'))
                
                self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} MCQs from CSV'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error reading CSV file: {e}'))
    
    def import_from_json(self, file_path):
        """Import MCQs from JSON file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                count = 0
                
                for item in data:
                    try:
                        domain, _ = Domain.objects.get_or_create(name=item['domain'])
                        topic, _ = Topic.objects.get_or_create(domain=domain, name=item['topic'])
                        subtopic, _ = Subtopic.objects.get_or_create(topic=topic, name=item['subtopic'])
                        
                        batch = None
                        if item.get('batch'):
                            batch, _ = Batch.objects.get_or_create(name=item['batch'])
                        
                        MCQ.objects.create(
                            domain=domain,
                            topic=topic,
                            subtopic=subtopic,
                            batch=batch,
                            difficulty=item.get('difficulty', 'Medium'),
                            tag=item.get('tag', ''),
                            question_text=item['question_text'],
                            option_a=item['option_a'],
                            option_b=item['option_b'],
                            option_c=item['option_c'],
                            option_d=item['option_d'],
                            correct_answer=item['correct_answer'].upper(),
                            reason=item['reason']
                        )
                        count += 1
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Error importing item: {e}'))
                
                self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} MCQs from JSON'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error reading JSON file: {e}'))
