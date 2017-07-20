# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from delionapi.serializers import *
from delionapi.models import *
from rest_framework import generics

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import permissions
from delionapi.permissions import IsOwnerOrReadOnly

class CategoryList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
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

class SearchList(APIView):

    def post(self, request, format=None):
        try:
            shop_object = Shop.objects.get(shop_name=request.data['name'])
            serializer = ShopSearchSerializer(shop_object)
            return Response(serializer.data)
        except:
            try:
                lifeinfo_object = LifeInfo.objects.get(lifeinfo_name=request.data['name'])
                serializer = LifeInfoSearchSerializer(lifeinfo_object)
                return Response(serializer.data)
            except:
                return Http404