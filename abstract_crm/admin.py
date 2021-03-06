#coding: utf-8

from django.contrib import admin
from models import Task, TaskStatus, Project, Priority, Tracker


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'priority')
    list_editable = ('user', 'status', 'priority')

admin.site.register(Project)
admin.site.register(Tracker)
admin.site.register(Task, TaskAdmin)
