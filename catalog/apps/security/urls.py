__author__ = 'eveR'

from django.conf.urls import patterns, url


urlpatterns = patterns('catalog.apps.security.views',
                url(r'^$', 'index_view',name="index"),
                )