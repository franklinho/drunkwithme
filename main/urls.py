from django.conf.urls import patterns, include, url

urlpatterns = patterns('main.views',
    url(r'^objects/drinks/(?P<drink_id>.*)/$','objects_drinks',name="main_objects_drink"),
    url(r'^objects/bars/(?P<bar_id>.*)/$','objects_bars',name="main_objects_bar"),
)
