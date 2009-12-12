import logging
import feedparser
import httplib
import urlparse
import time
import datetime
from pystories.models import NewsEntry, NewsTopic
from django.contrib.syndication.feeds  import Feed
from django.core.paginator import Paginator
import socket

from django.conf import settings
from django.contrib.syndication.feeds import FeedDoesNotExist
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F




#module logger use this logger in the standalone functions
mlogger = logging.getLogger(__name__)

#feedurl = "http://friendfeed.com/public?format=atom&service=googlereader&num=100"
#feedurl = "http://friendfeed.com/search?q=%s&who=everyone&service=googler&service=%s&format=atom&num="+settings.NUMBER_OF_ENTRIES
#News keywords
#services
ffservices = ['googlereader','delicious']
#keywords which we are looking for

SHARES_DECAY_FACTOR = 1.5
#Each time fetchfeed runs it sets the value of current shares to current shares/SHARES_DECAY_FACTOR


class FetchManager:
        
     def __init__(self):
         self.logger = logging.getLogger('%s.%s' % (__name__,self.__class__.__name__))
         
         
         
     def triggerfetchFeed(self):
          NewsEntry.objects.filter(noofshares__gt = 1).update(noofshares = F('noofshares')/SHARES_DECAY_FACTOR)
          
          for service in ffservices:
               self.logger.info("reading from %s" % service)
               topics = NewsTopic.objects.all()
               for topic in topics:
                    newsli = topic.get_keywords()
                    for tag in newsli :
                       furl =  "http://friendfeed.com/search?q=%s&service=%s&format=atom&num=%s" % (tag,service,settings.NUMBER_OF_ENTRIES)
                       self.logger.info("freiend feed url = %s "% furl)
                       self.fetchFeed(furl, topic)
         
         
            
      
     def fetchFeed(self,feedurl, topic):
          self.logger.info("Entering fetch feed function") 
          self.logger.info("fetching the feed from the friend feed")
          d = feedparser.parse(feedurl)
          self.logger.debug("how many entries %s" %len(d['entries'])) 
          #for each entry fetch its title and url
          self.logger.info("iterating filtering the feed entries and saving it to the database")
          for entry in d['entries']:
                #is it related to python / django / jquery
                #only if it is a valid url
                self.logger.debug("what is the value of entry link %s , %s" % (entry.link,entry.title) )
                if self.relatedToTopic(entry.title, topic):
                      burl  = self.bringBaseUrl(entry.link)
                      self.logger.debug("Base URL is (after eliminating the redirecting url's)  %s" % burl)
                      if burl :
                         #this entry is related to python save it in the database
                         self.logger.debug("preparing the NewsEntry object")
                         newslist = NewsEntry.objects.filter(url=burl, topic=topic)
                         self.logger.debug("length of newslist %s" % len(newslist))
                         if len(newslist) > 0 :
                              self.logger.debug("There is news entry with this URL  checking for duplicates......... ")
                              aflag = 0
                              oldentry = newslist[0]
                              lentryids = oldentry.entryids.split(";")
                              for eid in lentryids :
                                   if eid == entry.id :
                                        self.logger.info("not saving entry already exists")
                                        aflag = 1
                                        break
                                   
                              if aflag == 1 :
                                   continue
                              
                              self.logger.debug("The present entry is itself an unique one>> so increment the shares")
                              lentryids.append(entry.id)
                              oldentry.entryids = ";".join(lentryids)
                              oldentry.noofshares = oldentry.noofshares  + 1
                              oldentry.save()
                         else :
                              #creates a new entry now
                              self.logger.debug("There is no news entry with this URL so saving this ")
                              ne = NewsEntry(topic = topic)
                              ne.url = burl
                              #preprocess the title
                              start =  entry.title.find(":")
                              end = entry.title.find("(via")
                              if end == -1:
                                   end = len(entry.title)
                              ne.title = entry.title[start+1:end].strip()
                              print ne.url, ne.title, topic.slug
                              if(self.isItInEnglish(ne.title)) :
                                   ne.noofshares = 1
                                   self.logger.debug("published_parsed  date from universal feed parser %s" %entry.published_parsed)
                                   year,month,day,hour,min,second,asd,asdfk,asdfd = entry.published_parsed
                                   ne.publisheddate = datetime.datetime(year,month,day,hour,min,second)
                                   ne.pdate = datetime.date(year,month,day)
                                   self.logger.debug("publisheddate = %s pdate = %s" %(ne.publisheddate,ne.pdate))
                                   ne.entryids = entry.id
                                   ne.save()
                               
                                                        
     def isItInEnglish(self,title):
          self.logger.debug("checking whether the title is in english or not") 
#          for c in title:
#              if ord(c) >  256 :
#                    self.logger.debug("c = %s , interger = %d" %(c,ord(c)))
#                    return None
          return 1          
                              
                                   
          
     def relatedToTopic(self,title, topic):
          self.logger.info("Checking whether this entry is related to python,django or not")
          keywords = topic.get_keywords()
          stopwords =  topic.get_stop_words()
          #STowords beat keywords.
          for word in stopwords:
               if word and title.lower().find(word) >= 0 :
                    self.logger.debug("Found a stopword killing it, now. Stopword is: %s" % word)
                    return None
          
          for word in keywords:
               if word and title.lower().find(word) >= 0 :
                    self.logger.debug("this entry is related to python,django etc...")
                    return 1
                                             
          self.logger.debug("this entry is not related to python,django,jquery etc.....")                                   
          return None
     
     
     def bringBaseUrl(self,url):          
          self.logger.info("Bringing down the base URL")
          maxattempts = 5
          turl = url
          while (maxattempts  >  0) :
            self.logger.debug("what is the url=%s" % turl)
            host,path = urlparse.urlsplit(turl)[1:3]
            if  len(host.strip()) == 0 :
               return None
            #self.logger.debug("what is the host %s and path is %s"%(host,path))
            try: 
                    connection = httplib.HTTPConnection(host)
                    connection.request("HEAD", path)
                    resp = connection.getresponse()
                    #attempted
            except :
                     self.logger.debug("Could not open socket some network exception")
                     return None                     
            maxattempts = maxattempts - 1
            if (resp.status >= 300) and (resp.status <= 399):
                self.logger.debug("The present %s is a redirection one" %turl)
                turl = resp.getheader('location')
            elif (resp.status >= 200) and (resp.status <= 299) :
                self.logger.debug("The present url %s is a proper one" %turl)
                return turl
            else :
                #some problem with this url
                return None
               
          return None

     def getPopularNews(self, topic=None):
          self.logger.info("Fetching the poular news stories related to python django and jquery ")
          #get all the popular stories ordered by noofshares and date
          #get GMT-5 days date
          year,month,day,hour,min,second,asd,asdfk,asdfd = datetime.datetime.utctimetuple(datetime.datetime.now())
          todaygmt = datetime.date(year,month,day)
          self.logger.debug("what is the today GMT date %s" % todaygmt)
          self.logger.debug("what is the window size %s" % settings.WINDOW_SIZE)
          window_size_days = datetime.timedelta(days=settings.WINDOW_SIZE)
          #finding 5 days back date     
          window_size_days_ago = todaygmt - window_size_days
          self.logger.debug("5 days back GMT date %s" % window_size_days_ago)
          if topic:
               paginator = Paginator(NewsEntry.objects.filter(pdate__gte = window_size_days_ago, topic=topic).order_by('-noofshares','-publisheddate'),settings.WIDGET_PAGE_SIZE)
          else:
               paginator = Paginator(NewsEntry.objects.filter(pdate__gte = window_size_days_ago).order_by('-noofshares','-publisheddate'),settings.WIDGET_PAGE_SIZE)
          topnewslist = paginator.page(1)
          mlogger.debug("length topnewlist = %s " % len(topnewslist.object_list))
          return topnewslist.object_list
          #pass the list to the template
              
    

class LatestEntries(Feed) :
     title_template = 'pystories/feeds/title.html'
     description_template = 'pystories/feeds/description.html'

     
    # def __init__(self):
     #    self.logger = logging.getLogger('%s.%s' % (__name__,self.__class__.__name__))
     
     def get_object(self, bits):
          if len(bits) == 0:
               return NewsTopic.objects.get(slug = 'django')
          if not len(bits) == 1:
               raise ObjectDoesNotExist
          return NewsTopic.objects.get(slug = bits[0])
          
     def title(self, obj):
          return obj.title
     
     def link(self, obj):
          return obj.get_absolute_url()
          
     def description(self, obj):
          "Latest stories on %s" % ' '.join(obj.get_keywords())
         
     
     def item_link(self,obj):
          return obj.url
     
     def item_pubdate(self,obj):
           return obj.publisheddate                                   
     
     def items(self, obj):
          fmanager = FetchManager()
          return fmanager.getPopularNews(obj)
           

          
     