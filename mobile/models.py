from django.db import models
import json
import time
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

    @classmethod
    def get_or_create_user_profile(cls,user):
        try:
            profile = cls.objects.get(user=user)
        except cls.DoesNotExist:
            profile = cls(user=user)
            profile.save()

        return profile

    def level(self):
        level = min(6,self.num_drinks_consumed)
        return LEVEL_DRINK_MAP[level]

    def level_image(self):
        level = min(6,self.num_drinks_consumed)
        return LEVEL_IMAGE_MAP[level]

    @property
    def _redis_key(self):
        return "%s:::%s" % (self.user.id,self.id)

    def set_location(self,lat,lon,timestamp=time.time()):
        payload = {
            'latitude':lat,
            'longitude':lon,
            'timestamp':timestamp
            }
        cache.set(self._redis_key,json.dumps(payload))

    @property
    def latitude(self):
        return json.loads(cache.get(self._redis_key))['latitude'] if cache.has_key(self._redis_key) else None

    @property
    def longitude(self):
        return json.loads(cache.get(self._redis_key))['longitude'] if cache.has_key(self._redis_key) else None
        
        
