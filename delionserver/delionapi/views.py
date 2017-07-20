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

class MenuList(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopMenuSerializer

class LifeInfoList(generics.ListCreateAPIView):
    queryset = LifeInfo.objects.all()
    serializer_class = LifeInfoListSerializer

class LifeInfoDetail(generics.ListCreateAPIView):
    queryset = LifeInfo.objects.all()
    serializer_class = LifeInfoDetailSerializer