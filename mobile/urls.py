from django.conf.urls import patterns, include, url

urlpatterns = patterns('mobile.views',
    url(r'^$', 'index',name="mobile_index"),
    url(r'^drink/$', 'drink',name="mobile_drink"),
    url(r'^privacy/$','privacy',name="main_privacy"),
    url(r'^set-location/$','set_location',name="main_set_location"),
    url(r'^drink-action/$', 'drink_action',name="drink_action"),
    url(r'^drink-action/(?P<drink_id>.*)/$', 'drink_action',name="drink_action"),
    url(r'^checkin-action/(?P<bar_id>.*)/$', 'checkin_action',name="checkin_action"),
    url(r'^rank/$', 'rank',name="rank"),
    url(r'^stats/$', 'stats',name="stats")
)
