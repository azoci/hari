# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 08:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20171125_0803'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='item',
            table='ITEM',
        ),
    ]