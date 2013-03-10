from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from main.models import Drink, Bar

def objects_drinks(request,drink_id):
    drink = get_object_or_404(Drink,pk=drink_id)
    return render_to_response("drink.html",{'drink':drink},RequestContext(request))

def objects_bars(request,bar_id):
    bar = get_object_or_404(Bar,pk=bar_id)
    return render_to_response("bar.html",{'bar':bar},RequestContext(request))
