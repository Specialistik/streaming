# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-10 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_author_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Status', verbose_name='\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u0434\u043e\u0441\u0442\u0443\u043f\u0430'),
        ),
    ]
