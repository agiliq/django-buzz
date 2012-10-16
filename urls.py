from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

from django.conf import settings
import os
dirname = os.path.dirname(globals()["__file__"])



urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    (r'^pystories/',include('pystories.urls')),
    
)

if settings.DEBUG:    
    media_dir = os.path.join(dirname, 'site_media')
    urlpatterns += patterns('',
            url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': media_dir}),
        )

