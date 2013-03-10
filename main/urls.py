from django.conf.urls import patterns, include, url

urlpatterns = patterns('main.views',
    url(r'^objects/drinks/(?P<drink_id>.*)/$','objects_drinks',name="main_objects_drinks"),
)
