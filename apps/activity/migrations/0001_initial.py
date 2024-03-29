# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-08-21 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityManage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('category', models.IntegerField(choices=[(0, '商家活动'), (1, '平台活动')], verbose_name='活动分类')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='活动标题')),
                ('activity_img', models.ImageField(blank=True, null=True, upload_to='media/active', verbose_name='活动缩略图')),
                ('original_price', models.PositiveIntegerField(verbose_name='原价(单位分)')),
                ('activity_price', models.PositiveIntegerField(verbose_name='活动价(单位分)')),
                ('activity_start_time', models.DateTimeField(verbose_name='活动开始时间')),
                ('activity_end_time', models.DateTimeField(verbose_name='活动结束时间')),
                ('detail', models.TextField()),
            ],
            options={
                'verbose_name': '活动列表',
                'verbose_name_plural': '活动列表',
                'db_table': 'activity',
            },
        ),
    ]
