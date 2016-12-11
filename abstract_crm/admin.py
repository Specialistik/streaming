#coding: utf-8

from django.contrib import admin
from models import Task, TaskStatus

admin.site.register(Task)
admin.site.register(TaskStatus)
