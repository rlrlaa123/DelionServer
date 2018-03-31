# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .serializers import *
from .models import *
from rest_framework import generics

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

from rest_framework import filters
from django_filters import rest_framework as django_filters

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
    queryset = ShopLifeinfo.objects.all()
    serializer_class = ShopLifeinfoSerializer

class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShopLifeinfo.objects.all()
    serializer_class = ShopLifeinfoSerializer
#
class MenuList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SearchList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    queryset = ShopLifeinfo.objects.all()
    serializer_class = SearchSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name',]

# class IsOwnerFilterBackend(filters.BaseFilterBackend):
#     """
#     Filter that only allows users to see their own objects.
#     """
#     def filter_queryset(self, request, queryset, view):
#         search_fields = ('shop_name')
#         return queryset.filter(shop_name=search_fields)
#
# class SearchList(generics.ListAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly,)
#     serializer_class = SearchSerializer
#
#     def get_queryset(self):
#         query = self.request.query_params.get('query',None)
#         print query
#         shop = Shop.objects.filter(shop_name=query)
#         lifeinfo = Lifeinfo.objects.filter(lifeinfo_name=query)
#         all_results = list(shop)+list(lifeinfo)
#         print all_results
#         return all_results
#
