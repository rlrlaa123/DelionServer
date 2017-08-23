# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from serializers import *
from models import *
from rest_framework import generics

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import permissions
from permissions import IsOwnerOrReadOnly

from django_filters.rest_framework import DjangoFilterBackend

class CategoryList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ShopList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class MenuList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class LifeinfoList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
    queryset = Lifeinfo.objects.all()
    serializer_class = LifeinfoSerializer

class LifeinfoDetailList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
    queryset = Lifeinfo.objects.all()
    serializer_class = LifeinfoDetailSerializer

class LifeinfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lifeinfo.objects.all()
    serializer_class = LifeinfoDetailListSerializer

class SearchList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

    def post(self, request, format=None):
        try:
            shop_object = Shop.objects.get(shop_name=request.data['name'])
            serializer = ShopSearchSerializer(shop_object)
            filter_backends = (filters.SearchFilter,)
            search_fields = ('shop_name^',)

            return Response(serializer.data)
        except:
            try:
                lifeinfo_object = Lifeinfo.objects.get(lifeinfo_name=request.data['name'])
                serializer = LifeinfoSearchSerializer(lifeinfo_object)
                return Response(serializer.data)
            except:
                return Http404