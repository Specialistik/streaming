# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-08 19:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20161008_1902'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='audiostream',
            options={'verbose_name': '\u041f\u043e\u0442\u043e\u043a\u043e\u0432\u043e\u0435 \u0430\u0443\u0434\u0438\u043e', 'verbose_name_plural': '\u041f\u043e\u0442\u043e\u043a\u043e\u0432\u044b\u0435 \u0430\u0443\u0434\u0438\u043e'},
        ),
        migrations.AlterModelOptions(
            name='videostream',
            options={'verbose_name': '\u041f\u043e\u0442\u043e\u043a\u043e\u0432\u043e\u0435 \u0432\u0438\u0434\u0435\u043e', 'verbose_name_plural': '\u041f\u043e\u0442\u043e\u043a\u043e\u0432\u044b\u0435 \u0432\u0438\u0434\u0435\u043e'},
        ),
        migrations.AlterModelTable(
            name='audiostream',
            table='audio_streams',
        ),
        migrations.AlterModelTable(
            name='videostream',
            table='video_streams',
        ),
    ]
