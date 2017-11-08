#coding: utf-8

from django.contrib import admin
from videos.models import VideoCategory, Author, Video, History


class VideoCategoryAdmin(admin.ModelAdmin):
    exclude = ('keywords',)
    list_display = ('title', 'url')
    list_editable = ('url',)


class AuthorAdmin(admin.ModelAdmin):
    exclude = ('keywords',)
    list_display = ('title', 'url', 'profession', 'image', 'status')
    list_editable = ('url',)


class VideoAdmin(admin.ModelAdmin):
    exclude = ('keywords',)
    list_display = ('title', 'url')
    list_editable = ('url',)


admin.site.register(VideoCategory, VideoCategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(History)

