from delionapi.models import *
from rest_framework import serializers

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = (
            'category',
            'shop_or_lifeinfo',
        )

class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = (
            'category',
            'shop_name',
            'img',
            'branch',
            'phone',
            'openhour',
        )

class LifeInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LifeInfo
        fields = (
            'category',
            'lifeinfo_name',
            'img',
            'branch',
            'phone',
            'openhour',
            'address',
            'address_url',
        )

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = (
            'shop_name',
            'menu_name',
            'extender_menu',
            'price',
        )