# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 08:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('skey', models.IntegerField(db_column='SKEY', primary_key=True, serialize=False)),
                ('dt', models.CharField(db_column='DT', max_length=8)),
                ('mon', models.CharField(db_column='MON', max_length=2)),
                ('yr', models.CharField(db_column='YR', max_length=4)),
                ('qrtr', models.CharField(db_column='QRTR', max_length=20)),
                ('pd', models.CharField(blank=True, db_column='PD', max_length=45, null=True)),
                ('ayr', models.CharField(blank=True, db_column='AYR', max_length=6, null=True)),
                ('hyn', models.CharField(db_column='HYN', max_length=1)),
            ],
            options={
                'db_table': 'CALENDAR',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EvaluationFact',
            fields=[
                ('item_key', models.ForeignKey(db_column='ITEM_KEY', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='stock.Item')),
                ('unit', models.CharField(blank=True, db_column='UNIT', max_length=8, null=True)),
                ('tvalue', models.CharField(blank=True, db_column='TVALUE', max_length=200, null=True)),
                ('pvalue', models.CharField(blank=True, db_column='PVALUE', max_length=200, null=True)),
                ('ppvalue', models.CharField(blank=True, db_column='PPVALUE', max_length=200, null=True)),
            ],
            options={
                'db_table': 'EVALUATION_FACT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('pkey', models.IntegerField(db_column='PKEY', primary_key=True, serialize=False)),
                ('ckey', models.IntegerField(db_column='CKEY')),
                ('fnccd', models.CharField(db_column='FNCCD', max_length=10)),
                ('pacnt', models.CharField(db_column='PACNT', max_length=45)),
                ('cacnt', models.CharField(db_column='CACNT', max_length=45)),
                ('lvl', models.IntegerField(db_column='LVL')),
                ('seq', models.IntegerField(db_column='SEQ')),
                ('lyn', models.CharField(db_column='LYN', max_length=1)),
                ('myn', models.CharField(db_column='MYN', max_length=1)),
                ('pacnt_id', models.CharField(blank=True, db_column='PACNT_ID', max_length=30, null=True)),
                ('cacnt_id', models.CharField(blank=True, db_column='CACNT_ID', max_length=30, null=True)),
            ],
            options={
                'db_table': 'FINANCE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NoticeFact',
            fields=[
                ('item_key', models.ForeignKey(db_column='ITEM_KEY', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='stock.Item')),
                ('currency', models.CharField(db_column='CURRENCY', max_length=3)),
                ('tamt', models.DecimalField(blank=True, db_column='TAMT', decimal_places=2, max_digits=17, null=True)),
                ('pamt', models.DecimalField(blank=True, db_column='PAMT', decimal_places=2, max_digits=17, null=True)),
                ('ppamt', models.DecimalField(blank=True, db_column='PPAMT', decimal_places=2, max_digits=17, null=True)),
            ],
            options={
                'db_table': 'NOTICE_FACT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('pkey', models.IntegerField(db_column='PKEY', primary_key=True, serialize=False)),
                ('ckey', models.IntegerField(db_column='CKEY')),
                ('pfctr', models.CharField(db_column='PFCTR', max_length=45)),
                ('cfctr', models.CharField(db_column='CFCTR', max_length=45)),
                ('lvl', models.IntegerField(db_column='LVL')),
                ('seq', models.IntegerField(db_column='SEQ')),
                ('lyn', models.CharField(db_column='LYN', max_length=1)),
                ('myn', models.CharField(db_column='MYN', max_length=1)),
            ],
            options={
                'db_table': 'VALUE',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'managed': False},
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('skey', models.ForeignKey(db_column='SKEY', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='stock.Calendar')),
                ('mon', models.CharField(blank=True, db_column='MON', max_length=2, null=True)),
                ('smon', models.CharField(blank=True, db_column='SMON', max_length=2, null=True)),
                ('sdt', models.CharField(blank=True, db_column='SDT', max_length=8, null=True)),
                ('syr', models.CharField(blank=True, db_column='SYR', max_length=4, null=True)),
            ],
            options={
                'db_table': 'MONTH',
                'managed': False,
            },
        ),
    ]
