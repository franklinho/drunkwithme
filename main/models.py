from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Drink(models.Model):
    name=models.CharField(max_length=256)
    image = models.ImageField(upload_to="drinks")
    
    @property
    def facebook_object_url(self):
        return reverse("main_objects_drink",kwargs={'drink_id':self.id})