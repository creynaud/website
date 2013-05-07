from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^resume/$', views.resume, name='resume'),
    url(r'^sitemap\.xml$', views.sitemap, name='sitemap'),
    url(r'^cv\.html$', views.cv, name='cv'),
)
