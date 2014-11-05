# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StudyGroup'
        db.create_table(u'students_studygroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('monitor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['students.Student'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal(u'students', ['StudyGroup'])

        # Adding model 'Student'
        db.create_table(u'students_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('patronymic', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('bdate', self.gf('django.db.models.fields.DateField')()),
            ('student_card', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['students.StudyGroup'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal(u'students', ['Student'])


    def backwards(self, orm):
        # Deleting model 'StudyGroup'
        db.delete_table(u'students_studygroup')

        # Deleting model 'Student'
        db.delete_table(u'students_student')


    models = {
        u'students.student': {
            'Meta': {'object_name': 'Student'},
            'bdate': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['students.StudyGroup']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'patronymic': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'student_card': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'students.studygroup': {
            'Meta': {'object_name': 'StudyGroup'},
            'group_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['students.Student']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
        }
    }

    complete_apps = ['students']