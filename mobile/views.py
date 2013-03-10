from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
import facebook

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render_to_response("HelloMap.html",{},RequestContext(request))

@login_required
def check_in(request):
    graph = facebook.GraphAPI(request.user.social_auth.all()[0].extra_data['access_token'])

