from delionapi.models import *
from rest_framework import serializers

from versatileimagefield.serializers import VersatileImageFieldSerializer


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    img = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )
    class Meta:
        model = Category
        fields = (
            'category',
            'shop_or_lifeinfo',
            'img',
        )

class ShopSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField (many=Ture)

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



class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = (
            'menu_name',
            'extender_menu',
            'price',
        )

class ShopMenuSerializer(serializers.HyperlinkedModelSerializer):
    menu = MenuSerializer(many=True)

    class Meta:
        model = Shop
        fields = (
            'shop_name',
            'branch',
            'phone',
            'menu',
        )

class LifeinfoListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lifeinfo
        fields = (
            'category',
            'lifeinfo_name',
            'img',
            'branch',
            'phone',
            'address_url',
        )

class LifeinfoDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lifeinfo
        fields = (
            'lifeinfo_name',
            'branch',
            'phone',
            'address',
            'openhour',
        )

class ShopSearchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = (
            'shop_name',
            'branch',
            'phone',
            'img',
        )

class LifeinfoSearchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lifeinfo
        fields = (
            'lifeinfo_name',
            'branch',
            'phone',
            'address',
            'img',
        )