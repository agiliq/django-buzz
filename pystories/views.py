from django.http import HttpResponse
from django.core.paginator import Paginator
from django.template import Context , loader
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.contrib.sites.models import Site

from pystories.services.EntryService import FetchManager
from pystories.models import NewsEntry , Feedback, NewsTopic

import logging
import datetime

#Create module logger
#several logging configurations are configured in the models
mlogger = logging.getLogger(__name__)


def index(request, topic_slug=None):
     mlogger.info("Function index : view.py")
     fmanager = FetchManager()
     site = Site.objects.get_current()
     if not topic_slug:
          topic = None
          topnewslist =  fmanager.getPopularNews()
     else:
          topic = get_object_or_404(NewsTopic, slug = topic_slug)
          topnewslist =  fmanager.getPopularNews(topic = topic)
     data = {
               'topnewslist': topnewslist,
               'iframe_url': settings.IFRAME_URL,
               'site_url': settings.SITE_URL,
               'topic': topic,
               'site': site,
     }
     return render(request, "pystories/index.html", data)


def handleFeedback(request) :
     mlogger.info("handling the feedback")
     feedback = Feedback()
     feedback.flag = request.POST['feedback_value']
     mlogger.debug("what is the feedback="+feedback.flag)
     feedback.save()

     return HttpResponse("success","text")

def buildwidget(request, topic_slug=None) :
     mlogger.info("Function in buildwidget")
     fmanager = FetchManager()
     topic = get_object_or_404(NewsTopic, slug = topic_slug)
     site = Site.objects.get_current()
     topnewslist =  fmanager.getPopularNews(topic)
     data = {
               'topnewslist': topnewslist,
               'iframe_url': settings.IFRAME_URL,
               'site_url': settings.SITE_URL,
               'topic': topic,
               'site': site,
     }
     return render(request, "pystories/onlywidget.html", data)







