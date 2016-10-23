#coding: utf-8

from django.contrib import admin
from core.models import VideoCategory, Author, Video, VideoStreamSet, VideoStream, AudioStream

admin.site.register(VideoCategory)
admin.site.register(Author)
admin.site.register(Video)
admin.site.register(VideoStreamSet)
admin.site.register(VideoStream)
admin.site.register(AudioStream)
