# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-09 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streams', '0003_auto_20161201_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='videostream',
            name='time_end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='stream end time'),
        ),
        migrations.AddField(
            model_name='videostream',
            name='time_start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='stream start time'),
        ),
    ]
