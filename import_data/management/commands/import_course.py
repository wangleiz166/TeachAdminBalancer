import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from staffvModules.models import Course

# python manage.py import_courses path/to/your/csv/file.csv
class Command(BaseCommand):
    help = 'Imports courses from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                code = row['Code']
                linked_courses = row['Linked courses']
                unlinked_relatives = row['Unlinked relatives']
                name = row['Name']
                num_staff_allocated = int(row['Num staff allocated'])
                est_num_students = int(row['Est. Num Students'])
                hours = int(row['Credits'])

                # Create a datetime object for the create_time field
                create_time = datetime.now()

                # Create the Course object and save it
                course = Course(code=code, linked_courses=linked_courses, unlinked_relatives=unlinked_relatives,
                                name=name, num_staff_allocated=num_staff_allocated,
                                est_num_students=est_num_students, hours=hours, create_time=create_time)
                course.save()

        self.stdout.write(self.style.SUCCESS('Courses imported successfully!'))
