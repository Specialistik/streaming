# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 13:03
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20161113_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='author_deeds',
        ),
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.RemoveField(
            model_name='videostreamset',
            name='image',
        ),
        migrations.AlterField(
            model_name='audiostream',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='audiostream',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/audio_stream_pic', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='author',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/author', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='video',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/video_pic', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='videocategory',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='videocategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/category', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='videostream',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='videostream',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/video_stream_pic', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='videostreamset',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
    ]
