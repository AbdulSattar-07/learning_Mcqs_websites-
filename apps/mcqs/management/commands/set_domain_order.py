from django.core.management.base import BaseCommand
from apps.mcqs.models import Domain


class Command(BaseCommand):
    help = 'Set display order for domains based on their logical sequence'
    
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('=' * 70))
        self.stdout.write(self.style.SUCCESS('Setting Domain Display Order'))
        self.stdout.write(self.style.SUCCESS('=' * 70))
        
        # Define the correct order based on MCQ_BANK folder structure
        domain_order = {
            'Computer Networks': 1,
            'Computer Networks and Cloud Computing': 1,  # Alternative name
            'Programming': 2,
            'Data Structures': 3,
            'Operating Systems': 4,
            'Software Engineering': 5,
            'Web Development': 6,
            'AI/ML/Data Analytics': 7,
            'Cyber Security': 8,
            'Databases': 9,
            'Problem Solving and Analytical Skills': 10,
        }
        
        updated_count = 0
        
        for domain in Domain.objects.all():
            if domain.name in domain_order:
                order = domain_order[domain.name]
                domain.display_order = order
                domain.save()
                self.stdout.write(
                    self.style.SUCCESS(f'  ✓ {domain.name}: Order = {order}')
                )
                updated_count += 1
            else:
                # Set default order for unknown domains
                domain.display_order = 999
                domain.save()
                self.stdout.write(
                    self.style.WARNING(f'  ⚠ {domain.name}: Order = 999 (default)')
                )
                updated_count += 1
        
        self.stdout.write(self.style.SUCCESS('\n' + '=' * 70))
        self.stdout.write(self.style.SUCCESS(f'✓ Updated {updated_count} domains'))
        self.stdout.write(self.style.SUCCESS('=' * 70 + '\n'))
        
        # Show final order
        self.stdout.write(self.style.SUCCESS('Final Domain Order:'))
        for idx, domain in enumerate(Domain.objects.all().order_by('display_order', 'name'), 1):
            self.stdout.write(f'  {idx}. {domain.name} (order: {domain.display_order})')
