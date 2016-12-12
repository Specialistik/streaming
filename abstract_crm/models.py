#coding: utf-8

import os
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from core.models import List

class Project(List):
    class Meta:
       db_table = 'projects'
       verbose_name = u'Проект'
       verbose_name_plural = u'Проекты'


class TaskStatus(List):
    class Meta:
       db_table = 'task_statuses'
       verbose_name = u'Статус задачи'
       verbose_name_plural = u'Статусы задач'



class Task(models.Model):
    title = models.CharField(max_length=80, verbose_name=u"Заголовок")
    description = RichTextField(verbose_name=u"Описание")
    project = models.ForeignKey(Project, verbose_name=u'Проект') 
    user = models.ForeignKey(User, verbose_name=u'Пользователь') 
    status = models.ForeignKey(TaskStatus, verbose_name=u"Статус")
    time_creation = models.DateTimeField(default=datetime.now(), verbose_name=u'Время создания')
    time_end = models.DateTimeField(null=True, blank=True, verbose_name=u'Время завершения')


    def __repr__(self):
        return self.title if self.title is not None else u'empty'

    def __str__(self):
        return self.title if self.title is not None else u'empty'

    def __unicode__(self):
        return self.title if self.title is not None else u'empty'


    class Meta:
       db_table = 'tasks'
       verbose_name = u'Задача'
       verbose_name_plural = u'Задачи'


