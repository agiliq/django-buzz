
from south.db import db
from django.db import models
from pystories.models import *

class Migration:
    
    def forwards(self, orm):
        
        
        # Adding model 'Feedback'
        db.create_table('pystories_feedback', (
            ('id', orm['pystories.Feedback:id']),
            ('publisheddate', orm['pystories.Feedback:publisheddate']),
            ('flag', orm['pystories.Feedback:flag']),
        ))
        db.send_create_signal('pystories', ['Feedback'])
        
        # Adding model 'NewsEntry'
        db.create_table('pystories_newsentry', (
            ('id', orm['pystories.NewsEntry:id']),
            ('url', orm['pystories.NewsEntry:url']),
            ('title', orm['pystories.NewsEntry:title']),
            ('description', orm['pystories.NewsEntry:description']),
            ('noofshares', orm['pystories.NewsEntry:noofshares']),
            ('ispopular', orm['pystories.NewsEntry:ispopular']),
            ('pdate', orm['pystories.NewsEntry:pdate']),
            ('publisheddate', orm['pystories.NewsEntry:publisheddate']),
            ('populardate', orm['pystories.NewsEntry:populardate']),
            ('entryids', orm['pystories.NewsEntry:entryids']),
        ))
        db.send_create_signal('pystories', ['NewsEntry'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Feedback'
        db.delete_table('pystories_feedback')
        
        # Deleting model 'NewsEntry'
        db.delete_table('pystories_newsentry')
        
    
    
    models = {
        'pystories.feedback': {
            'flag': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publisheddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'pystories.newsentry': {
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'entryids': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ispopular': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'noofshares': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pdate': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'populardate': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'publisheddate': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
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
