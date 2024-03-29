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
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('order_sn', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='订单号')),
                ('trade_no', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='交易号')),
                ('total_money', models.PositiveIntegerField(verbose_name='总金额(单位分)')),
                ('handel_money', models.PositiveIntegerField(verbose_name='手续费(单位分)')),
                ('user_real_money', models.PositiveIntegerField(verbose_name='用户实际支付(单位分)')),
                ('store_real_money', models.PositiveIntegerField(verbose_name='商家实收金额(单位分)')),
                ('pay_type', models.IntegerField(choices=[(0, '微信支付'), (1, '余额支付')], verbose_name='支付方式')),
                ('pay_status', models.IntegerField(choices=[(0, '未支付'), (1, '已完成'), (2, '已取消')], verbose_name='支付状态')),
                ('order_status', models.IntegerField(choices=[(0, '已取消'), (1, '待使用'), (2, '待评价'), (3, '已完成')], verbose_name='订单状态')),
                ('order_type', models.IntegerField(choices=[(0, '洗车订单'), (1, '活动订单'), (2, '充值订单')], verbose_name='订单类型')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
                'db_table': 'order',
            },
        ),
    ]
