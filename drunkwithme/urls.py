from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'', include('mobile.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
)
