# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-08-21 11:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('money', models.PositiveIntegerField(null=True, verbose_name='充值金额')),
            ],
            options={
                'verbose_name': '充值金额',
                'verbose_name_plural': '充值金额',
                'db_table': 'Recharge',
            },
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='网站标题')),
                ('keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name='网站关键字')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='网站描述')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='system', verbose_name='网站logo')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='地址')),
                ('jifen_chongzhi', models.IntegerField(blank=True, null=True, verbose_name='积分重置日期')),
                ('jifen_max', models.FloatField(blank=True, null=True, verbose_name='每日积分上限')),
                ('qrcode_day', models.IntegerField(blank=True, null=True, verbose_name='二维码有效期')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='邮箱')),
                ('beiancode', models.CharField(blank=True, max_length=100, null=True, verbose_name='备案号')),
                ('wechat', models.CharField(blank=True, max_length=100, null=True, verbose_name='微信')),
                ('company_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='公司名称')),
                ('phone', models.IntegerField(blank=True, null=True, verbose_name='联系电话')),
            ],
            options={
                'verbose_name': '网站设置',
                'verbose_name_plural': '网站设置',
                'db_table': 'system',
            },
        ),
        migrations.AddField(
            model_name='recharge',
            name='system',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.System', verbose_name='系统'),
        ),
        migrations.CreateModel(
            name='Qrcode',
            fields=[
            ],
            options={
                'verbose_name': '二维码设置',
                'verbose_name_plural': '二维码设置',
                'proxy': True,
                'indexes': [],
            },
            bases=('system.system',),
        ),
        migrations.CreateModel(
            name='SetPoint',
            fields=[
            ],
            options={
                'verbose_name': '积分设置',
                'verbose_name_plural': '积分设置',
                'proxy': True,
                'indexes': [],
            },
            bases=('system.system',),
        ),
    ]
