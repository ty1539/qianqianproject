# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-08-21 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitymanage',
            name='storemanage',
            field=models.ManyToManyField(to='store.StoreManage', verbose_name='商家'),
        ),
    ]
