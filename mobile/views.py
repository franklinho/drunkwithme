from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import RequestContext
from django.conf import settings
from mobile.models import Drink, Bar, UserProfile
import facebook
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    user_profiles = UserProfile.objects.all().order_by("-num_drinks_consumed")
    bars = Bar.objects.all().order_by("name")
    return render_to_response("index.html",{'bars':bars, 'user_profiles':user_profiles},RequestContext(request))

@login_required
def drink_action(request,drink_id):
    profile = UserProfile.get_or_create_profile(request.user)
    profile.num_drinks_consumed+=1
    profile.save()
    return HttpResponse("OK")

@login_required
def checkin_action(request,bar_id):
    bar = get_object_or_404(Bar,pk=bar_id)
    profile = UserProfile.get_or_create_profile(request.user)
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
