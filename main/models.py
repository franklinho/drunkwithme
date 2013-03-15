from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from main.constants import LEVEL_CHOICES

# Create your models here.
class Drink(models.Model):
    name=models.CharField(max_length=256)
    image = models.ImageField(upload_to="drinks")
    
    @property
    def facebook_object_url(self):
        return reverse("main_objects_drink",kwargs={'drink_id':self.id})


class Bar(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    latitude = models.FloatField()
    longitude = models.FloatField()
    priority = models.IntegerField()


    @property
    def facebook_object_url(self):
        return reverse("main_objects_bar",kwargs={'bar_id':self.id})

class User(models.Model):
    name = models.CharField(max_length=256)
    rank = models.IntegerField()
    drinks = models.IntegerField()
    bars = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    drunk_level = models.IntegerField(default=0,choices = LEVEL_CHOICES)

    @classmethod
    def get_or_create_user_profile(cls,user):
        try:
            profile = cls.objects.get(user=user)
        except cls.DoesNotExist:
            profile = cls(user=user)
            profile.save()

        return profile
        
        
