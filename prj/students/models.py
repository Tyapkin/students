# -*- coding: utf-8 -*-
from django.db import models
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.utils.http import urlquote


class Person(models.Model):
    #Абстрактный класс описывающий человека.
    name = models.CharField(max_length=64, verbose_name='name')
    slug = models.SlugField(max_length=64, verbose_name='slug field')
    surname = models.CharField(max_length=64, verbose_name='surname')
    patronymic = models.CharField(max_length=64, verbose_name='patronymic')
    email = models.EmailField(blank=True, null=True, verbose_name='email')
    bdate = models.DateField(verbose_name='date of birth')

    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'persons'
        abstract = True

    def get_absolute_url(self):
        return urlquote('/person/{0}/'.format(self.id))

    def get_full_name(self):
        full_name = '%s %s' % (
            self.name.encode('utf-8'),
            self.surname.encode('utf-8'))
        return full_name.strip()

    def short_name(self):
        return self.name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])


class StudyGroup(models.Model):
    group_name = models.CharField(max_length=64, verbose_name='group name')
    slug = models.SlugField(max_length=64, verbose_name='slug')
    monitor = models.ForeignKey(
        'Student',
        verbose_name='monitor',
        on_delete=models.SET_NULL,
        blank=True, null=True)

    class Meta:
        verbose_name = 'study group'
        verbose_name_plural = 'study groups'

    def __str__(self):
        return '%s' % self.group_name.encode('utf-8')

    def get_absolute_url(self):
        return urlquote(reverse('group_detail'), args=[str(self.id)])


class Student(Person):
    student_card = models.CharField(
        max_length=12, verbose_name='number of student card')
    group = models.ForeignKey(
        StudyGroup, verbose_name='study group',
        on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return urlquote(reverse('student_detail', args=[str(self.id)]))
