# Django settings for doloto project.

from localsettings import *

import os

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 't9eow#2=q94y4xh=+3&0(m#v)4n(&zm))2%euv2h)jc!0uumu!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)



INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'pystories'
)

#number of entries has to fecthed each time from friendfeed
NUMBER_OF_ENTRIES = '20'

#use for determining the popular stories 
WINDOW_SIZE = 2

#LOG_FILE_PATH in django
LOG_FILE_PATH = "\""+os.path.join(os.path.join(os.path.dirname(os.path.normpath(__file__)),'logs'),"logs.txt")+"\""

#LOG FILE NAME In django 
logfilename =  os.path.join(os.path.dirname(os.path.normpath(__file__)),'logging.conf')
LOG_FILE_NAME = logfilename

#number of entries to be displayed on the widget
WIDGET_PAGE_SIZE = 10


