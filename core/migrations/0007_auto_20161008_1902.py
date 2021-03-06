# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-08 19:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20161004_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioStream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=80, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('keywords', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('stream_source', models.CharField(max_length=200, verbose_name='\u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a \u043f\u043e\u0442\u043e\u043a\u043e\u0432\u043e\u0433\u043e \u0430\u0443\u0434\u0438\u043e')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoStream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=80, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('keywords', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('stream_source', models.CharField(max_length=200, verbose_name='\u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a \u043f\u043e\u0442\u043e\u043a\u043e\u0432\u043e\u0433\u043e \u0432\u0438\u0434\u0435\u043e')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoStreamSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=80, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('keywords', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
            ],
            options={
                'db_table': 'video_stream_sets',
                'verbose_name': '\u0421\u0435\u0442 \u0432\u0438\u0434\u0435\u043e',
                'verbose_name_plural': '\u0421\u0435\u0442\u044b \u0432\u0438\u0434\u0435\u043e',
            },
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': '\u0412\u0438\u0434\u0435\u043e', 'verbose_name_plural': '\u0412\u0438\u0434\u0435\u043e'},
        ),
        migrations.AlterModelOptions(
            name='videocategory',
            options={'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0432\u0438\u0434\u0435\u043e', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0432\u0438\u0434\u0435\u043e'},
        ),
        migrations.AlterField(
            model_name='video',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.VideoCategory', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='video',
            name='keywords',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_url',
            field=models.CharField(max_length=256, verbose_name='URL \u0432\u0438\u0434\u0435\u043e'),
        ),
        migrations.AlterField(
            model_name='videocategory',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='videocategory',
            name='keywords',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430'),
        ),
        migrations.AlterField(
            model_name='videocategory',
            name='pid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.VideoCategory', verbose_name='\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0430\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='videocategory',
            name='title',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
        migrations.AddField(
            model_name='videostream',
            name='stream_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.VideoStreamSet', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
    ]
