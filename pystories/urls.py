from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib.syndication.views import feed

from pystories.services.EntryService import LatestEntries


feeds = {
    'recent': LatestEntries
}


urlpatterns = patterns('pystories.views',
    (r'^welcome/$','index'),
    (r'^postfeedback/$','handleFeedback'),
     (r'^widget/$','buildwidget'),
     (r'^feeds/(?P<url>.*)/$', feed , {'feed_dict': feeds})
    )
