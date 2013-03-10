from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response("HelloMap.html",{},RequestContext(request))

def map(request):
    return render_to_response("HelloMap.html",{},RequestContext(request))

def drink(request):
    return render_to_response("Drink.html",{},RequestContext(request))