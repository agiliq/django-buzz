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


class NewsEntry(models.Model):
      url = models.URLField(max_length=1024,db_index=True)
      title = models.CharField(max_length=1024)
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
      
      
class Feedback(models.Model):
      publisheddate = models.DateTimeField(auto_now=True)
      flag = models.CharField(max_length=10)
      
      
      def __unicode__(self):
            return "Feedback is %s %s" %(publisheddate,flag)
            
