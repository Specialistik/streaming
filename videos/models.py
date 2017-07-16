#coding: utf-8

from __future__ import unicode_literals

from django.db import models
from core.models import Substance, Status, Profile


class VideoCategory(Substance):
    pid = models.ForeignKey("self", null=True, blank=True, verbose_name=u"Родительская категория")

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
    category = models.ForeignKey(VideoCategory, verbose_name=u"Категория")
    profession = models.CharField(max_length=80, verbose_name=u"Профессия")
    image = models.ImageField(upload_to='author', verbose_name=u"Фото")
    status = models.ForeignKey(Status, verbose_name=u'Уровень доступа')

    def get_url(self):
        return '/author/' + str(self.id) + '/' + self.url

    class Meta:
        db_table = 'authors'
        verbose_name = u'Автор'
        verbose_name_plural = u'Авторы'


# todo: thumbs generation for videos
class Video(Substance):
    author = models.ForeignKey(Author, verbose_name=u"Автор")
    video = models.FileField(upload_to='video', verbose_name=u"Видео")

    def get_url(self):
        return '/video/' + str(self.id) + '/' + self.url

    def get_thumb(self):
        return '/static/images/no_thumbnail.jpg'

    class Meta:
        db_table = 'videos'
        verbose_name = u'Видео'
        verbose_name_plural = u'Видео'


class History(models.Model):
    profile = models.ForeignKey(Author, editable=False, verbose_name=u"Пользьватель")
    video = models.ForeignKey(Video, editable=False, verbose_name=u"Просмотренное видео")
    time = models.DateTimeField(auto_now=True, editable=False, verbose_name=u"Время просмотра")

    class Meta:
        db_table = 'video_history'
        verbose_name = u'Просмотр видео'
        verbose_name_plural = u'Просмотры видео'
