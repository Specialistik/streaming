#coding: utf-8

from __future__ import unicode_literals
import os
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField


class Substance(models.Model):
    title = models.CharField(max_length=80, verbose_name=u"Заголовок")
    keywords = models.CharField(max_length=256, null=True, blank=True, verbose_name=u"Ключевые слова")
    description = RichTextField(null=True, blank=True, verbose_name=u"Описание")
    url = models.CharField(max_length=80, verbose_name=u'Человеко-понятный URL')

    def __repr__(self):
        return self.title if self.title is not None else u'empty'

    def __str__(self):
        return self.title if self.title is not None else u'empty'

    def __unicode__(self):
        return self.title if self.title is not None else u'empty'

    class Meta:
        abstract=True
        
        
class List(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Название')

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        abstract=True


class Article(Substance):

    def get_url(self):
        return '/article/' + str(self.id)

    class Meta:
        db_table = 'articles'
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'


class Status(List):
    class Meta:
       db_table = 'statuses'
       verbose_name = u'Уровень доступа'
       verbose_name_plural = u'Уровни доступа'
       
       
class Profession(List):
    class Meta:
       db_table = 'professions'
       verbose_name = u'Профессия'
       verbose_name_plural = u'Профессии'
