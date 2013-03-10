from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = patterns('',
    url(r'', include('mobile.urls')),
    url(r'', include('social_auth.urls')),
    url(r'', include('main.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += staticfiles_urlpatterns()
