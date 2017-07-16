#coding: utf-8

from sorl.thumbnail.admin import AdminImageMixin
from django.contrib import admin
from streams.models import VideoStreamSet, VideoStream


class VideoStreamSetAdmin(AdminImageMixin, admin.ModelAdmin):

    exclude = ('keywords',)
    list_display = ('title', 'url')
    list_editable = ('url',)


class VideoStreamAdmin(admin.ModelAdmin):
    exclude = ('keywords',)
    list_display = ('title', 'url')
    list_editable = ('url',)


admin.site.register(VideoStreamSet, VideoStreamSetAdmin)
admin.site.register(VideoStream, VideoStreamAdmin)

