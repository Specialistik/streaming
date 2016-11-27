#coding: utf-8

from django.contrib import admin
from streams.models import VideoStreamSet, VideoStream, AudioStream

admin.site.register(VideoStreamSet)
admin.site.register(VideoStream)
admin.site.register(AudioStream)

