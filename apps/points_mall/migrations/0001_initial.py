# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-08-21 11:23
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('discount_coupon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogisticsCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='物流公司名称')),
            ],
            options={
                'verbose_name': '物流公司',
                'verbose_name_plural': '物流公司',
                'db_table': 'logistics_company',
            },
        ),
        migrations.CreateModel(
            name='LuckyShopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('luckyshopping_type', models.IntegerField(choices=[(0, '抽奖商品')], verbose_name='抽奖商品类型')),
            ],
            options={
                'verbose_name': '抽奖商品',
                'verbose_name_plural': '抽奖商品',
                'db_table': 'lucky_shopping',
            },
        ),
        migrations.CreateModel(
            name='PointOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('phone', models.CharField(max_length=11, verbose_name='联系电话')),
                ('order_status', models.IntegerField(choices=[(0, '未发货'), (1, '已发货'), (2, '已完成')], default=0, verbose_name='积分商城订单状态')),
                ('tracking_number', models.PositiveIntegerField(blank=True, null=True, verbose_name='物流单号')),
                ('logistics_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='points_mall.LogisticsCompany', verbose_name='物流公司')),
                ('luckyshopping', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='points_mall.LuckyShopping', verbose_name='抽奖商品')),
            ],
            options={
                'verbose_name': '积分商城订单',
                'verbose_name_plural': '积分商城订单',
                'db_table': 'point_order',
            },
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('shopping_type', models.IntegerField(choices=[(0, '实物商品'), (1, '优惠券商品')], verbose_name='商品分类')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='商品名称')),
                ('need_point', models.BigIntegerField(blank=True, null=True, verbose_name='商品兑换所需积分')),
                ('color', models.CharField(blank=True, max_length=100, null=True, verbose_name='颜色')),
                ('size', models.CharField(blank=True, max_length=200, null=True, verbose_name='规格')),
                ('weight', models.IntegerField(default=0, verbose_name='重量')),
                ('repertory', models.IntegerField(default=0, verbose_name='库存')),
                ('detail', DjangoUeditor.models.UEditorField(default='', verbose_name='商品详情')),
                ('shopping_img', models.ImageField(blank=True, null=True, upload_to='media/shopping', verbose_name='商品封面图片')),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discount_coupon.Discount', verbose_name='优惠券')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'db_table': 'shopping',
            },
        ),
        migrations.CreateModel(
            name='TaskManage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('one_time_point', models.PositiveIntegerField(default=0, verbose_name='单次签到积分')),
                ('all_month_point', models.PositiveIntegerField(default=0, verbose_name='满月获取的积分')),
                ('invite_point', models.PositiveIntegerField(default=0, verbose_name='邀请获得积分')),
                ('consume_point', models.PositiveIntegerField(default=0, verbose_name='消费获得积分')),
                ('recharge_point', models.PositiveIntegerField(default=0, verbose_name='充值获得积分')),
                ('share_point', models.PositiveIntegerField(default=0, verbose_name='分享获得积分')),
                ('comment_point', models.PositiveIntegerField(default=0, verbose_name='评论获得积分')),
            ],
            options={
                'verbose_name': '任务',
                'verbose_name_plural': '任务',
                'db_table': 'task_manage',
            },
        ),
        migrations.AddField(
            model_name='pointorder',
            name='shopping',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='points_mall.Shopping', verbose_name='非抽奖商品'),
        ),
    ]