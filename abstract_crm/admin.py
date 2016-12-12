#coding: utf-8

from django.contrib import admin
from models import Task, TaskStatus, Project, Priority

admin.site.register(Task)
admin.site.register(TaskStatus)
admin.site.register(Project)
admin.site.register(Priority)
