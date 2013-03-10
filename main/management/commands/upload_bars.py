from django.core.management.base import BaseCommand, CommandError
from main.models import Bar
import os
import csv

dir_path = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))

class Command(BaseCommand):
    def handle(self, *args, **options):
        reader = csv.reader(open("%s/BarLocations.csv" % dir_path,"rb").read())
        for line in reader:
            if not Bar.objects.filter(name=line[0]).exists():
                Bar(name=line[0],
                    address=line[1],
                    latitude=line[2],
                    longitude=line[3],
                    priority=line[4]).save()
