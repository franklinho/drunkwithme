from django.db import models
import json
import time
import facebook
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.cache import cache

from mobile.constants import (LEVEL_DRINK_MAP,
                              LEVEL_IMAGE_MAP)

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

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    num_drinks_consumed = models.IntegerField(default=0)
    num_bars_visited = models.IntegerField(default=0)
    first_name = models.CharField(max_length=128,null=True,blank=True)
    last_name = models.CharField(max_length=128,null=True,blank=True)

    @property
    def full_name(self):
        if not self.first_name or not self.last_name:
            graph = facebook.GraphAPI(self.user.social_auth.all()[0].extra_data['access_token'])
            profile = graph.get_object("me")
            self.first_name = profile['first_name']
            self.last_name = profile['last_name']
            self.save()

        return "%s %s" % (self.first_name,self.last_name)
        

    @classmethod
    def get_or_create_user_profile(cls,user):
        try:
            profile = cls.objects.get(user=user)
        except cls.DoesNotExist:
            profile = cls(user=user)
            profile.save()

        return profile

    def level(self):
        level = min(19,self.num_drinks_consumed)
        return LEVEL_DRINK_MAP[level]

    def level_number(self):
        return min(19,self.num_drinks_consumed)+1

    def level_image(self):
        level = min(19,self.num_drinks_consumed)
        return LEVEL_IMAGE_MAP[level]

    @property
    def _redis_key(self):
        return "%s:::%s" % (self.user.id,self.id)

    def set_location(self,lat,lon,timestamp=time.time()):
        payload = {
            'latitude':float(lat),
            'longitude':float(lon),
            'timestamp':timestamp
            }
        cache.set(self._redis_key,json.dumps(payload))

    @property
    def latitude(self):
        return json.loads(cache.get(self._redis_key))['latitude'] if cache.has_key(self._redis_key) else 37.7712748

    @property
    def longitude(self):
        return json.loads(cache.get(self._redis_key))['longitude'] if cache.has_key(self._redis_key) else -122.4425378
        
        

from django.db.models.signals import post_save

# User
def user_post_save(sender, instance, signal, *args, **kwargs):
    # Creates user profile
    profile, new = UserProfile.objects.get_or_create(user=instance)

post_save.connect(user_post_save,sender=User)
