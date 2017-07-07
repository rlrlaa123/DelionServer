# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from delionapi.serializers import *
from delionapi.models import *
from rest_framework import generics

# Create your views here.
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ShopList(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class LifeInfoList(generics.ListCreateAPIView):
    queryset = LifeInfo.objects.all()
    serializer_class = LifeInfoSerializer

class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer