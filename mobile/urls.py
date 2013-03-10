from django.conf.urls import patterns, include, url

urlpatterns = patterns('mobile.views',
    url(r'^$', 'index',name="mobile_index"),
    url(r'^check_in/$', 'check_in',name="mobile_check_in"),
    url(r'^map/$', 'map',name="map"),
    url(r'^drink/$', 'drink',name="drink"),
    url(r'^rank/$', 'rank',name="rank"),
    url(r'^stats/$', 'stats',name="stats")
)
