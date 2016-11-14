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


class VideoCategory(Substance):
    pid = models.ForeignKey("self", null=True, blank=True, verbose_name=u"Родительская категория")
    image = models.ImageField(upload_to='category', null=True, blank=True, verbose_name=u"Картинка")

    def get_url(self):
	return '/category/' + self.id + '/' + self.url
        
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
	return '/author/' + self.id + '/' + self.url
 
    class Meta:
        db_table = 'authors'
        verbose_name = u'Автор'
        verbose_name_plural = u'Авторы'
    
    
class Video(Substance):
    author = models.ForeignKey(Author, null=True, verbose_name=u"Автор")
    video_url = models.CharField(max_length=256, verbose_name=u"URL видео")
    image = models.ImageField(upload_to='media/video_pic', null=True, blank=True, verbose_name=u"Картинка")

    def get_url(self):
	return '/video/' + self.id + '/' + self.url
 

    def thumb(self):
	return '/static/images/ch1.jpg'

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
    image = models.ImageField(upload_to='video_stream_pic', null=True, blank=True, verbose_name=u"Картинка")

    def get_url(self):
	return '/videostream/' + self.id + '/' + self.url
 

    class Meta:
        db_table = 'video_streams'
        verbose_name = u'Потоковое видео'
        verbose_name_plural = u'Потоковые видео'
    
    
class AudioStream(Substance):
    stream_source = models.CharField(max_length=200, verbose_name=u"Источник потокового аудио")
    image = models.ImageField(upload_to='audio_stream_pic', null=True, blank=True, verbose_name=u"Картинка")

    def get_url(self):
	return '/audiostream/' + self.id + '/' + self.url
 
    class Meta:
        db_table = 'audio_streams'
        verbose_name = u'Потоковое аудио'
        verbose_name_plural = u'Потоковые аудио'
