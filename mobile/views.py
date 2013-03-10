from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import RequestContext
from django.conf import settings
from main.models import Drink
import facebook

from django.contrib.auth.decorators import login_required

def index(request):
    return render_to_response("HelloMap.html",{},RequestContext(request))

def drink_action(request,drink_id):
    graph = facebook.GraphAPI(request.user.social_auth.all()[0].extra_data['access_token'])
    drink = get_object_or_404(Drink,pk=drink_id)
    graph.put_object("me","drunkwithmeapp:take",drink="%s%s" % (settings.DOMAIN_URL,drink.facebook_object_url))
    return HttpResponse("OK")
    
def map(request):
    return render_to_response("HelloMap.html",{},RequestContext(request))

def drink(request):
    return render_to_response("Drink.html",{},RequestContext(request))


def whoami(request):
    return HttpResponse(request.user)
