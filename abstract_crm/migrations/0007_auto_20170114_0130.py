# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-13 22:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstract_crm', '0006_auto_20161216_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time_creation',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 14, 1, 30, 18, 197243), verbose_name='\u0412\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
    ]
