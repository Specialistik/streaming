#coding: utf-8

from __future__ import unicode_literals

from django.db import models
from core.models import Substance, Status


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
    status = models.ForeignKey(Status, verbose_name=u'status')

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
        return '/static/images/ch1.jpg'

#    def save(self, *args, **kw):
#	if ((self.video.name.lower()[-4:] != '.mp4') or (self.video.name.lower()[-5:] != '.webm')):
#	    raise Exception('wrong video format')
#	super(Video, self).save(self, *args, **kw)

    class Meta:
        db_table = 'videos'
        verbose_name = u'Видео'
        verbose_name_plural = u'Видео'
