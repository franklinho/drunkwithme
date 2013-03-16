from django.core.management.base import BaseCommand, CommandError
from django.core.files.images import ImageFile
from mobile.models import Drink
import os
import json

dir_path = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))

class Command(BaseCommand):
    def handle(self, *args, **options):
        drinks_data = json.loads(open("%s/drinks.json" % dir_path,"rb").read())
        for drink in drinks_data['drinks']:
            if not Drink.objects.filter(name=drink['name']).exists():
                image_file = "%s/images/%s" % (dir_path,drink['image'])

                drinkobj = Drink(name=drink['name'])
                drinkobj.image.save(drink['image'],ImageFile(open(image_file,"rb")))
                drinkobj.save()
                
