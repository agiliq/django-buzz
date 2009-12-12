
from south.db import db
from django.db import models
from pystories.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Creating unique_together for [topic, url] on NewsEntry.
        db.create_unique('pystories_newsentry', ['topic_id', 'url'])
        
    
    
    def backwards(self, orm):
        
        # Deleting unique_together for [topic, url] on NewsEntry.
        db.delete_unique('pystories_newsentry', ['topic_id', 'url'])
        
    
    
    models = {
        'pystories.feedback': {
            'flag': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publisheddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'pystories.newsentry': {
            'Meta': {'unique_together': "(('topic', 'url'),)"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'entryids': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ispopular': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'noofshares': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pdate': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'populardate': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'publisheddate': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pystories.NewsTopic']", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '1024', 'db_index': 'True'})
        },
        'pystories.newstopic': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'stop_words': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }
    
    complete_apps = ['pystories']
