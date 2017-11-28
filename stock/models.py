# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Calendar(models.Model):
    skey = models.IntegerField(db_column='SKEY', primary_key=True)  # Field name made lowercase.
    dt = models.CharField(db_column='DT', max_length=8)  # Field name made lowercase.
    mon = models.CharField(db_column='MON', max_length=2)  # Field name made lowercase.
    yr = models.CharField(db_column='YR', max_length=4)  # Field name made lowercase.
    qrtr = models.CharField(db_column='QRTR', max_length=20)  # Field name made lowercase.
    pd = models.CharField(db_column='PD', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ayr = models.CharField(db_column='AYR', max_length=6, blank=True, null=True)  # Field name made lowercase.
    hyn = models.CharField(db_column='HYN', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CALENDAR'


class EvaluationFact(models.Model):
    item_key = models.ForeignKey('Item', models.DO_NOTHING, db_column='ITEM_KEY', primary_key=True)  # Field name made lowercase.
    value_pkey = models.ForeignKey('Value', models.DO_NOTHING, db_column='VALUE_PKEY',related_name='evaluationfact_value_pkey')  # Field name made lowercase.
    value_ckey = models.ForeignKey('Value', models.DO_NOTHING, db_column='VALUE_CKEY',related_name='evaluationfact_value_ckey')  # Field name made lowercase.
    calendar_key = models.ForeignKey(Calendar, models.DO_NOTHING, db_column='CALENDAR_KEY')  # Field name made lowercase.
    unit = models.CharField(db_column='UNIT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    tvalue = models.CharField(db_column='TVALUE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pvalue = models.CharField(db_column='PVALUE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ppvalue = models.CharField(db_column='PPVALUE', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVALUATION_FACT'
        unique_together = (('item_key', 'value_pkey', 'value_ckey', 'calendar_key'),)


class Finance(models.Model):
    pkey = models.IntegerField(db_column='PKEY', primary_key=True)  # Field name made lowercase.
    ckey = models.IntegerField(db_column='CKEY')  # Field name made lowercase.
    fnccd = models.CharField(db_column='FNCCD', max_length=10)  # Field name made lowercase.
    pacnt = models.CharField(db_column='PACNT', max_length=45)  # Field name made lowercase.
    cacnt = models.CharField(db_column='CACNT', max_length=45)  # Field name made lowercase.
    lvl = models.IntegerField(db_column='LVL')  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ')  # Field name made lowercase.
    lyn = models.CharField(db_column='LYN', max_length=1)  # Field name made lowercase.
    myn = models.CharField(db_column='MYN', max_length=1)  # Field name made lowercase.
    pacnt_id = models.CharField(db_column='PACNT_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cacnt_id = models.CharField(db_column='CACNT_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FINANCE'
        unique_together = (('pkey', 'ckey'),)


class Item(models.Model):
    skey = models.AutoField(db_column='SKEY', primary_key=True)  # Field name made lowercase.
    nm = models.CharField(db_column='NM', max_length=20)  # Field name made lowercase.
    cd = models.CharField(db_column='CD', max_length=6)  # Field name made lowercase.
    biznm = models.CharField(db_column='BIZNM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bizcd = models.CharField(db_column='BIZCD', max_length=6, blank=True, null=True)  # Field name made lowercase.
    stktm = models.CharField(db_column='STKTM', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mrktm = models.CharField(db_column='MRKTM', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cbiznm = models.CharField(db_column='CBIZNM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pros = models.CharField(db_column='PROS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cons = models.CharField(db_column='CONS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    attr = models.CharField(db_column='ATTR', max_length=5, blank=True, null=True)  # Field name made lowercase.
    stknum = models.DecimalField(db_column='STKNUM', max_digits=17, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    eqcap = models.DecimalField(db_column='EQCAP', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    facevl = models.DecimalField(db_column='FACEVL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='CURRENCY', max_length=3, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    f_yn = models.CharField(db_column='F_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    yn = models.CharField(db_column='YN', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITEM'


class Month(models.Model):
    skey = models.ForeignKey(Calendar, models.DO_NOTHING, db_column='SKEY', primary_key=True)  # Field name made lowercase.
    mon = models.CharField(db_column='MON', max_length=2, blank=True, null=True)  # Field name made lowercase.
    smon = models.CharField(db_column='SMON', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sdt = models.CharField(db_column='SDT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    syr = models.CharField(db_column='SYR', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MONTH'


class NoticeFact(models.Model):
    item_key = models.ForeignKey(Item, models.DO_NOTHING, db_column='ITEM_KEY', primary_key=True)  # Field name made lowercase.
    finance_pkey = models.ForeignKey(Finance, models.DO_NOTHING, db_column='FINANCE_PKEY',related_name='noticefact_value_pkey')  # Field name made lowercase.
    finance_ckey = models.ForeignKey(Finance, models.DO_NOTHING, db_column='FINANCE_CKEY',related_name='noticefact_value_ckey')  # Field name made lowercase.
    month_key = models.ForeignKey(Month, models.DO_NOTHING, db_column='MONTH_KEY')  # Field name made lowercase.
    currency = models.CharField(db_column='CURRENCY', max_length=3)  # Field name made lowercase.
    tamt = models.DecimalField(db_column='TAMT', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pamt = models.DecimalField(db_column='PAMT', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ppamt = models.DecimalField(db_column='PPAMT', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOTICE_FACT'
        unique_together = (('item_key', 'finance_pkey', 'finance_ckey', 'month_key'),)


class Value(models.Model):
    pkey = models.IntegerField(db_column='PKEY', primary_key=True)  # Field name made lowercase.
    ckey = models.IntegerField(db_column='CKEY')  # Field name made lowercase.
    pfctr = models.CharField(db_column='PFCTR', max_length=45)  # Field name made lowercase.
    cfctr = models.CharField(db_column='CFCTR', max_length=45)  # Field name made lowercase.
    lvl = models.IntegerField(db_column='LVL')  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ')  # Field name made lowercase.
    lyn = models.CharField(db_column='LYN', max_length=1)  # Field name made lowercase.
    myn = models.CharField(db_column='MYN', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VALUE'
        unique_together = (('pkey', 'ckey'),)


class EventHist(models.Model):
    skey = models.AutoField(db_column='SKEY', primary_key=True)  # Field name made lowercase.
    dt = models.CharField(db_column='DT', max_length=8)  # Field name made lowercase.
    nm = models.CharField(db_column='NM', max_length=20)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=500)  # Field name made lowercase.
    rate = models.DecimalField(db_column='RATE', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVENT_HIST'

class TradeHist(models.Model):
    skey = models.AutoField(db_column='SKEY', primary_key=True)  # Field name made lowercase.
    dt = models.CharField(db_column='DT', max_length=8)  # Field name made lowercase.
    type_nm = models.CharField(db_column='TYPE_NM', max_length=10)  # Field name made lowercase.
    item_key = models.ForeignKey(Item, models.DO_NOTHING, db_column='ITEM_KEY')  # Field name made lowercase.
    num = models.DecimalField(db_column='NUM', max_digits=17, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='PRICE', max_digits=17, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    amt = models.DecimalField(db_column='AMT', max_digits=17, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRADE_HIST'

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
