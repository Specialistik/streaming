#coding: utf-8

from django.contrib import admin
from videos.models import VideoCategory, Author, Video


admin.site.register(VideoCategory)
admin.site.register(Author)
admin.site.register(Video)

