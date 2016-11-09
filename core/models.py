#coding: utf-8
from __future__ import unicode_literals



import os
from django.db import models
from django.conf import settings

#PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
#os.path.join(BASE_DIR, "static")


class Substance(models.Model):
    title = models.CharField(max_length=80, null=True, blank=True, verbose_name=u"Заголовок")
    keywords = models.CharField(max_length=20, null=True, blank=True, verbose_name=u"Ключевые слова")
    description = models.CharField(max_length=200, null=True, blank=True, verbose_name=u"Описание")
    image = models.ImageField(null=True, blank=True, verbose_name=u"Картинка")

    def __unicode__(self):
        return self.title
    
    class Meta:
        abstract=True

class VideoCategory(Substance):
    pid = models.ForeignKey("self", null=True, blank=True, verbose_name=u"Родительская категория")
        
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
    name = models.CharField(max_length=80, null=True, blank=True, verbose_name=u"Ник/Имя автора")
    author_deeds = models.TextField(null=True, blank=True, verbose_name=u"Краткое описание")
    profession = models.CharField(max_length=80, null=True, blank=True, verbose_name=u"profession")    

    class Meta:
        db_table = 'authors'
        verbose_name = u'Автор'
        verbose_name_plural = u'Авторы'
    
    
class Video(Substance):
    author = models.ForeignKey(Author, null=True, verbose_name=u"Автор")
    video_url = models.CharField(max_length=256, verbose_name=u"URL видео")

    class Meta:
        db_table = 'videos'
        verbose_name = u'Видео'
        verbose_name_plural = u'Видео'
        
        
class VideoStreamSet(Substance):
    
    def children(self):
        return VideoStream.objects.filter(stream_set=self.id)
    
    class Meta:
        db_table = 'video_stream_sets'
        verbose_name = u'Сет потокового видео'
        verbose_name_plural = u'Сеты потокового видео'
        

class VideoStream(Substance):
    stream_set = models.ForeignKey(VideoStreamSet, verbose_name=u"Категория")
    stream_source = models.CharField(max_length=200, verbose_name=u"Источник потокового видео")
    
    class Meta:
        db_table = 'video_streams'
        verbose_name = u'Потоковое видео'
        verbose_name_plural = u'Потоковые видео'
    
    
class AudioStream(Substance):
    stream_source = models.CharField(max_length=200, verbose_name=u"Источник потокового аудио")
    
    class Meta:
        db_table = 'audio_streams'
        verbose_name = u'Потоковое аудио'
        verbose_name_plural = u'Потоковые аудио'
