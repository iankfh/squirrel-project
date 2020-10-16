from django.core.management.base import BaseCommand, CommandError
from squirrel.models import SquirrelSighting
from datetime import datetime
import csv

class Command(BaseCommand):
    help = 'Export the squirrel csv'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_file')

    def handle(self, *args, **options):
        output  = []
        
        myset = SquirrelSighting.objects.all()

        file_ = options['squirrel_file']

        with open(file_, 'a') as fp:
            writer = csv.writer(fp)
            writer.writerow(['Unique Squirrel ID', 'Latitude', 'Longitude', 'Shift', 'Date', 'Age'])
            for obj in myset:
                output.append([obj.unique_squirrel_id, obj.latitude, obj.longitude, obj.shift, obj.date, obj.age])
            writer.writerows(output)        
                
        msg = f'You are exporting to (file_)'
        self.stdout.write(self.style.SUCCESS(msg))
