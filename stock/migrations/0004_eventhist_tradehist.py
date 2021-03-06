# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20171125_0839'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventHist',
            fields=[
                ('skey', models.AutoField(db_column='SKEY', primary_key=True, serialize=False)),
                ('dt', models.CharField(db_column='DT', max_length=8)),
                ('nm', models.CharField(db_column='NM', max_length=20)),
                ('content', models.CharField(db_column='CONTENT', max_length=500)),
                ('rate', models.DecimalField(blank=True, db_column='RATE', decimal_places=2, max_digits=17, null=True)),
            ],
            options={
                'db_table': 'EVENT_HIST',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TradeHist',
            fields=[
                ('skey', models.AutoField(db_column='SKEY', primary_key=True, serialize=False)),
                ('dt', models.CharField(db_column='DT', max_length=8)),
                ('type_nm', models.CharField(db_column='TYPE_NM', max_length=10)),
                ('num', models.DecimalField(blank=True, db_column='NUM', decimal_places=0, max_digits=17, null=True)),
                ('price', models.DecimalField(blank=True, db_column='PRICE', decimal_places=0, max_digits=17, null=True)),
                ('amt', models.DecimalField(blank=True, db_column='AMT', decimal_places=0, max_digits=17, null=True)),
                ('content', models.CharField(db_column='CONTENT', max_length=500)),
            ],
            options={
                'db_table': 'TRADE_HIST',
                'managed': False,
            },
        ),
    ]
