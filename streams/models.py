#coding: utf-8

from __future__ import unicode_literals

from django.db import models
from core.models import Substance

class VideoStreamSet(Substance):
    pic = models.ImageField(upload_to='video_stream_set_pic', verbose_name=u"Картинка")

    def children(self):
        return VideoStream.objects.filter(stream_set=self.id)

    def has_active_stream(self):
	return (VideoStream.objects.filter(stream_set=self.id, active=True).exists())

    def active_stream(self):
	return VideoStream.objects.get(stream_set=self.id, active=True).stream_source

    class Meta:
        db_table = 'video_stream_sets'
        verbose_name = u'Видео канал'
        verbose_name_plural = u'Видео каналы'


class VideoStream(Substance):
    stream_set = models.ForeignKey(VideoStreamSet, verbose_name=u"Категория")
    stream_source = models.CharField(max_length=200, verbose_name=u"Источник потокового видео")
    pic = models.ImageField(upload_to='video_stream_pic', null=True, blank=True, verbose_name=u"Картинка")
    active = models.BooleanField(default=False, verbose_name=u'Активный стрим')

    def get_url(self):
        return '/video_stream/' + str(self.id) + '/' + self.url

    class Meta:
        db_table = 'video_streams'
        verbose_name = u'Потоковое видео'
        verbose_name_plural = u'Потоковые видео'


class AudioStream(Substance):
    stream_source = models.CharField(max_length=200, verbose_name=u"Источник потокового аудио")
    image = models.ImageField(upload_to='audio_stream_pic', null=True, blank=True, verbose_name=u"Картинка")

    def get_url(self):
        return '/audio_stream/' + str(self.id) + '/' + self.url

    class Meta:
        db_table = 'audio_streams'
        verbose_name = u'Потоковое аудио'
        verbose_name_plural = u'Потоковые аудио'


