from django.shortcuts import render_to_response
from django.template import RequestContext
from main.models import Drink

def objects_drinks(request,drink_id):
    drink = get_object_or_404(Drink,pk=drink_id)
    return render_to_response("drink.html",{'drink':drink},RequestContext(request))
