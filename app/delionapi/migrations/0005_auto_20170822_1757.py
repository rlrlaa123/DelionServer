# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-22 08:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delionapi', '0004_auto_20170720_1647'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='lifeinfo',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'managed': False},
        ),
    ]