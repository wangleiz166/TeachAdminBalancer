from django.core.management.base import BaseCommand
from staff.models import Staff
from faker import Faker

class Command(BaseCommand):
    help = 'Generate random staff data'

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(10):  # Generate 10 staff records
            staff = Staff(
                initials=fake.random_letter(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                cat='Assistant',
                probation_year=fake.random_digit(),
                annual_availability=fake.random_int(min=0, max=100),
                unadjusted_max=fake.random_int(min=0, max=100),
                adjusted_max=fake.random_int(min=0, max=100),
                availability_notes=fake.text(),
                employment_end_date=fake.date_between(start_date='-1y', end_date='+1y'),
                probation_start_date=fake.date_between(start_date='-1y', end_date='+1y'),
                probation_start_year_stage=fake.word(),
            )
            staff.save()

        self.stdout.write(self.style.SUCCESS('Random staff data has been generated.'))
