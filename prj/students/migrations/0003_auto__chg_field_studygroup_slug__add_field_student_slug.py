# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'StudyGroup.slug'
        db.alter_column(u'students_studygroup', 'slug', self.gf('django.db.models.fields.SlugField')(default=datetime.datetime(2014, 10, 28, 0, 0), max_length=64))
        # Adding field 'Student.slug'
        db.add_column(u'students_student', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default=datetime.datetime(2014, 10, 28, 0, 0), max_length=64),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'StudyGroup.slug'
        db.alter_column(u'students_studygroup', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=64, null=True))
        # Deleting field 'Student.slug'
        db.delete_column(u'students_student', 'slug')


    models = {
        u'students.student': {
            'Meta': {'object_name': 'Student'},
            'bdate': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['students.StudyGroup']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'patronymic': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64'}),
            'student_card': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'students.studygroup': {
            'Meta': {'object_name': 'StudyGroup'},
            'group_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['students.Student']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['students']