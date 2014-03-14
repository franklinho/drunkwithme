import time

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, Http404
from django.template import RequestContext
from mobile.models import Drink, Bar, UserProfile
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    user_profiles = UserProfile.objects.all().order_by("-num_drinks_consumed")
    bars = Bar.objects.all().order_by("name")
    return render_to_response("index.html",{'bars':bars,
                                            'user_profiles':user_profiles,
                                            'current_profile':request.user.get_profile()
                                            },RequestContext(request))

@login_required
def set_location(request):
    latitude = request.GET.get("latitude",None)
    longitude = request.GET.get("longitude",None)
    if latitude and longitude:
        request.user.get_profile().set_location(latitude,longitude,time.time())
    return HttpResponse("OK")

@login_required
def drink_action(request,drink_id=None):
    profile = request.user.get_profile()
    profile.num_drinks_consumed+=1
    profile.save()
    return HttpResponse("OK")

@login_required
def checkin_action(request,bar_id):
    bar = get_object_or_404(Bar,pk=bar_id)
    profile = request.user.get_profile()
    profile.set_location(bar.latitude,bar.longitude)
    profile.num_bars_visited+=1
    profile.save()
    return HttpResponse("OK")

@login_required
def drink(request):
    drink_options = Drink.objects.all().order_by("name")
    return render_to_response("Drink.html",{'drink_options':drink_options},RequestContext(request))

@login_required
def rank(request):
    user_profiles = UserProfile.objects.all().order_by("-num_drinks_consumed")
    return render_to_response("Rank.html",
                              {'user_profiles':user_profiles},
                              RequestContext(request))

@login_required
def stats(request):
    return HttpResponse("Not Implemented Yet")

def privacy(request):
    return render_to_response("privacy.html",{},RequestContext(request))
