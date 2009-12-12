from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib.syndication.views import feed

from pystories.services.EntryService import LatestEntries


feeds = {
    'recent': LatestEntries
}


urlpatterns = patterns('pystories.views',
    url(r'^$','index', {'topic_slug':'django'}),
    url(r'^welcome/$','index', {'topic_slug':'django'}),
    url(r'^widget/$','buildwidget', {'topic_slug':'django'}),
    url(r'^postfeedback/$','handleFeedback'),
    url(r'^widget/(?P<topic_slug>.*)/$','buildwidget', name='pystories_widget'),
    url(r'^feeds/(?P<url>.*)/$', feed , {'feed_dict': feeds}),
    url(r'^(?P<topic_slug>.*)/$','index', name='pystories_page'),
    
    )
