__author__ = 'TOSHIBA'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'facebook_aggregator_pilot.views.index', name='index'),
    )