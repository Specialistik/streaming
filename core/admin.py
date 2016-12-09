#coding: utf-8

from django.contrib import admin
from core.models import Article, Status

admin.site.register(Article)
admin.site.register(Status)
