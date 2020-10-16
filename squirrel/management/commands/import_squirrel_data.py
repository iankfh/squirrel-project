from django.core.management.base import BaseCommand, CommandError
from squirrel.models import SquirrelSighting
from datetime import datetime
import csv

class Command(BaseCommand):
    help = 'Import the squirrel csv'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_file')

    def handle(self, *args, **options):
        file_ = options['squirrel_file']

        with open(file_) as fp:
            reader = csv.DictReader(fp)

            for item in reader:
                obj = SquirrelSighting()
                obj.unique_squirrel_id = item['Unique Squirrel ID']
                obj.latitude = item['X']
                obj.longitude = item['Y']
                obj.shift = item['Shift']
                obj.date = datetime.strptime(item['Date'], '%m%d%Y').date()
                obj.age = item['Age']

                
                try:
                   obj.save()
                except:
                   continue
                
                
        msg = f'You are importing from (file_)'
        self.stdout.write(self.style.SUCCESS(msg))
