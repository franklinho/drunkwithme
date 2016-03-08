from django.core.management.base import BaseCommand, CommandError
from mobile.models import Bar
import os
import csv
import pdb

dir_path = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))

class Command(BaseCommand):
    def handle(self, *args, **options):
        file = open("%s/BarLocations.csv" % dir_path,"rb")
        lines = file.read().split("\r")
        for line in lines:
            data = [l.replace("\r","") for l in line.split(",")]
            if not Bar.objects.filter(name=data[0]).exists():
                Bar(name=data[0],
                    address=data[1],
                    latitude=float(data[2]),
                    longitude=float(data[3]),
                    priority=int(data[4])).save()
