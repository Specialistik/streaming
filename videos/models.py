#coding: utf-8

from __future__ import unicode_literals

from django.db import models
from core.models import Substance


class VideoCategory(Substance):
    pid = models.ForeignKey("self", null=True, blank=True, verbose_name=u"Родительская категория")
    image = models.ImageField(upload_to='category', null=True, blank=True, verbose_name=u"Картинка")

    def get_url(self):
        return '/category/' + str(self.id) + '/' + self.url

    def children(self):
        return VideoCategory.objects.filter(pid=self.id)

    def has_children(self):
        if len(VideoCategory.objects.filter(pid=self.id)) > 0:
            return True
        return False

    class Meta:
        db_table = 'video_cats'
        verbose_name = u'Категория видео'
        verbose_name_plural = u'Категории видео'


class Author(Substance):
    category = models.ForeignKey(VideoCategory, null=True, blank=True, verbose_name=u"Категория")
    profession = models.CharField(max_length=80, null=True, blank=True, verbose_name=u"profession")
    image = models.ImageField(upload_to='media/author', null=True, blank=True, verbose_name=u"Картинка")

    def get_url(self):
        return '/author/' + str(self.id) + '/' + self.url

    class Meta:
        db_table = 'authors'
        verbose_name = u'Автор'
        verbose_name_plural = u'Авторы'


class Video(Substance):
    author = models.ForeignKey(Author, null=True, verbose_name=u"Автор")
    video_url = models.CharField(max_length=256, verbose_name=u"URL видео")
    pic = models.ImageField(upload_to='media/video_pic', null=True, blank=True, verbose_name=u"Картинка")

    def get_url(self):
        return '/video/' + str(self.id) + '/' + self.url

    def get_thumb(self):
        return '/static/images/ch1.jpg'

    class Meta:
        db_table = 'videos'
        verbose_name = u'Видео'
        verbose_name_plural = u'Видео'
