
from south.db import db
from django.db import models
from pystories.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'NewsTopic'
        db.create_table('pystories_newstopic', (
            ('id', orm['pystories.NewsTopic:id']),
            ('title', orm['pystories.NewsTopic:title']),
            ('slug', orm['pystories.NewsTopic:slug']),
            ('keywords', orm['pystories.NewsTopic:keywords']),
            ('stop_words', orm['pystories.NewsTopic:stop_words']),
        ))
        db.send_create_signal('pystories', ['NewsTopic'])
        
        
        # Adding field 'NewsEntry.topic'
        db.add_column('pystories_newsentry', 'topic', orm['pystories.newsentry:topic'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'NewsTopic'
        db.delete_table('pystories_newstopic')
        
        # Deleting field 'NewsEntry.topic'
        db.delete_column('pystories_newsentry', 'topic_id')
        
    
    
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
