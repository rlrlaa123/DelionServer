# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delionapi', '0009_auto_20170822_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopLifeinfo',
            fields=[
                ('shop_lifeinfo_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('img', models.CharField(blank=True, max_length=45, null=True)),
                ('img_ppoi', models.CharField(blank=True, max_length=45, null=True)),
                ('branch', models.CharField(blank=True, max_length=45, null=True)),
                ('phone', models.CharField(max_length=45)),
                ('openhour', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.CharField(blank=True, max_length=225, null=True)),
                ('address_url', models.CharField(blank=True, max_length=225, null=True)),
            ],
            options={
                'db_table': 'shop_lifeinfo',
                'managed': False,
            },
        ),
    ]
