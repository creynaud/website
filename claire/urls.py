from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^resume/$', views.resume, name='resume'),
)
