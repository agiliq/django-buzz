from django.db import models
from django.conf import settings
import logging
import logging.config
import os

logfilename =  os.path.join(os.path.dirname(os.path.normpath(os.sys.modules[settings.SETTINGS_MODULE].__file__)),'logging.conf')

# Create your models here.
#loading the logging configuration
logging.config.fileConfig(settings.LOG_FILE_NAME,defaults=dict(log_path=settings.LOG_FILE_PATH))


#Create module logger
mlogger = logging.getLogger(__name__)
mlogger.debug("From settins LOG_FILE_NAME  %s LOG_FILE_PATH  %s" % (settings.LOG_FILE_NAME,settings.LOG_FILE_PATH))

class NewsTopic(models.Model):
      title = models.CharField(max_length=1000)
      slug = models.SlugField()
      keywords = models.TextField(help_text = "Comma separted field of values to search for.", default="")
      stop_words = models.TextField(help_text = "Comma separted field of values which kill the story.",  null = True, blank=True)
      
      def __unicode__(self):
            return self.title
      
      @models.permalink
      def get_absolute_url(self):
            return ('pystories_page', [], {'topic_slug': self.slug})
      
      def get_keywords(self):
            return [el.strip() for el in self.keywords.split(',')]
            
      def get_stop_words(self):
            return [el.strip() for el in self.stop_words.split(',')]

class NewsEntry(models.Model):
      topic = models.ForeignKey(NewsTopic, null = True, blank=True)
      url = models.URLField(max_length=1000,db_index=True)
      title = models.CharField(max_length=1000)
      description = models.TextField(null=True)
      noofshares = models.IntegerField(default=0)
      ispopular = models.BooleanField(default=0)
      #To facilitate the fast retrieval for the queries involving the date
      pdate = models.DateField(db_index=True)
      publisheddate = models.DateTimeField()
      populardate = models.DateTimeField(null=True)
      entryids = models.TextField(default='')
      
      def __unicode__(self):
            return self.url
      
      class Meta:
            unique_together = ('topic', 'url', )
      
      
class Feedback(models.Model):
      publisheddate = models.DateTimeField(auto_now=True)
      flag = models.CharField(max_length=10)
      
      
      def __unicode__(self):
            return "Feedback is %s %s" %(publisheddate,flag)
            
