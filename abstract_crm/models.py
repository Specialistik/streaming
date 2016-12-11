#coding: utf-8

import os
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from core.models import List


class TaskStatus(List):
    class Meta:
       db_table = 'task_statuses'
       verbose_name = u'task status'
       verbose_name_plural = u'task statuses'



class Task(models.Model):
    title = models.CharField(max_length=80, verbose_name=u"Заголовок")
    description = RichTextField(verbose_name=u"Описание")
    user = models.ForeignKey(User, verbose_name=u'django user') 
    status = models.ForeignKey(TaskStatus, verbose_name=u"task status")
    time_creation = models.DateTimeField(null=True, blank=True, verbose_name=u'task creation time')
    time_end = models.DateTimeField(null=True, blank=True, verbose_name=u'task end time')


    def __repr__(self):
        return self.title if self.title is not None else u'empty'

    def __str__(self):
        return self.title if self.title is not None else u'empty'

    def __unicode__(self):
        return self.title if self.title is not None else u'empty'


    class Meta:
       db_table = 'tasks'
       verbose_name = u'task'
       verbose_name_plural = u'tasks'


