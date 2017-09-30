# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField

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


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(unique=True, max_length=45)
    shop_or_lifeinfo = models.CharField(max_length=45, blank=True, null=True)
    img = VersatileImageField(
        'Image',
        upload_to='img/',
        ppoi_field='img_ppoi',
        blank=True
    )
    img_ppoi = PPOIField()

    class Meta:
        managed = False
        db_table = 'category'


class DelionapiCategory(models.Model):
    category = models.CharField(primary_key=True, max_length=10)
    shop_or_lifeinfo = models.CharField(max_length=8, blank=True, null=True)
    img = models.CharField(max_length=100)
    img_ppoi = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'delionapi_category'


class DelionapiLifeinfo(models.Model):
    category = models.CharField(max_length=8)
    lifeinfo_name = models.CharField(max_length=45)
    img = models.CharField(max_length=70, blank=True, null=True)
    branch = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    openhour = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45)
    address_url = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'delionapi_lifeinfo'


class DelionapiMenu(models.Model):
    created = models.DateTimeField()
    menu_name = models.CharField(max_length=45)
    extender_menu = models.CharField(max_length=45, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    shop_name = models.ForeignKey('DelionapiShop', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'delionapi_menu'


class DelionapiShop(models.Model):
    category = models.CharField(max_length=8)
    shop_name = models.CharField(unique=True, max_length=45)
    img = models.CharField(max_length=70, blank=True, null=True)
    branch = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    openhour = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delionapi_shop'


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


class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    shop = models.ForeignKey('ShopLifeinfo', models.DO_NOTHING)
    menu_name = models.CharField(max_length=45)
    extender_menu = models.CharField(max_length=45)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class ShopLifeinfo(models.Model):
    shop_lifeinfo_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    name = models.CharField(max_length=45)
    img = VersatileImageField(
        'Image',
        upload_to='img/',
        ppoi_field='img_ppoi',
        blank=True
    )
    img_ppoi = PPOIField()
    branch = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45)
    openhour = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=225, blank=True, null=True)
    address_url = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_lifeinfo'
