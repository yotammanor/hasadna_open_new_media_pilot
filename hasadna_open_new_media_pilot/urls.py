from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hasadna_open_new_media_pilot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^facebook/', include('facebook_aggregator_pilot.urls', namespace='facebook_aggregator_pilot')),
    url(r'^admin/', include(admin.site.urls)),
)
