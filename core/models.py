#coding: utf-8

from __future__ import unicode_literals
import os
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField


class Substance(models.Model):
    title = models.CharField(max_length=80, null=True, blank=True, verbose_name=u"Заголовок")
    keywords = models.CharField(max_length=20, null=True, blank=True, verbose_name=u"Ключевые слова")
    description = RichTextField(null=True, blank=True, verbose_name=u"Описание")
    url = models.CharField(max_length=80, null=True, blank=True, verbose_name=u'Человеко-понятный URL')

    def __repr__(self):
        return self.title if self.title is not None else u'empty'

    def __str__(self):
        return self.title if self.title is not None else u'empty'

    def __unicode__(self):
        return self.title if self.title is not None else u'empty'

    class Meta:
        abstract=True




class Article(Substance):

    def get_url(self):
        return '/article/' + str(self.id)

    class Meta:
        db_table = 'articles'

