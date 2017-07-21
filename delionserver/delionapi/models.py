# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    category = models.CharField(primary_key=True,max_length=10,default='test')
    shop_or_lifeinfo = models.CharField(max_length=8,null='test')
    img = models.CharField(max_length=70, null=True, blank=True)

class Shop(models.Model):
    category = models.CharField(max_length=8,default='test')
    shop_name = models.CharField(max_length=45,default='test',unique=True)
    img = models.CharField(max_length=70,null=True, blank =True)
    # 빼도 될 것 같음.. 추후에 같은 이름에 다른 지점의 식당이 있을 경우는 shop_name을 'shop_name branch_name' 으로 입력하면 됨
    branch = models.CharField(max_length=45,null=True, blank =True)
    phone = models.CharField(max_length=45,null=True, blank =True)
    openhour = models.CharField(max_length=45,null=True, blank =True)

class LifeInfo(models.Model):
    category = models.CharField(max_length=8,default='test')
    lifeinfo_name = models.CharField(max_length=45,default='test')
    img = models.CharField(max_length=70,null=True, blank =True)
    branch = models.CharField(max_length=45,null=True, blank =True)
    phone = models.CharField(max_length=45,null=True, blank =True)
    openhour = models.CharField(max_length=45,null=True, blank =True)
    address = models.CharField(max_length=45,default='test')
    address_url = models.CharField(max_length=100,default='test')

class Menu(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    shop_name = models.ForeignKey(Shop,to_field='shop_name')
    menu_name = models.CharField(max_length=45,default='test')
    extender_menu = models.CharField(max_length=45,null=True, blank =True)
    price = models.IntegerField(null=True, blank =True)

    class Meta:
        ordering = ('created',)

class Csv(models.Model):
    csv = models.FileField(upload_to='%Y/%m/%d/datafile')
#년/월/일 형식으로 정적 파일이 저장 된다
