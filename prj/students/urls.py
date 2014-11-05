# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import GroupList, Group, StudentDetail, AddStudent, EditStudent, DeleteStudent

urlpatterns = patterns(
    '',
    url(r'^group-list/$', GroupList.as_view(), name='group_list'),

    url(r'^group/(?P<pk>\d+)/$', Group.as_view(), name='group_detail'),

    url(r'^student/(?P<pk>\d+)/$',
        StudentDetail.as_view(), name='student_detail'),

    url(r'^student/add/$', AddStudent.as_view(), name='student_add'),

    url(r'^student/(?P<pk>\d+)/edit/$',
        EditStudent.as_view(), name='edit_student'),

    url(r'^student/(?P<pk>\d+)/delete/$',
        DeleteStudent.as_view(), name='delete_student'),

    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'students/login.html'}),

    url(r'^logout/$', 'students.views.logout', name='logout'),
)
