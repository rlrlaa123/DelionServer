from models import *
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
            'category_id',
            'category',
            'shop_or_lifeinfo',
            'img',
        )

class ShopSerializer(serializers.HyperlinkedModelSerializer):
    img = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )
    categoryid = serializers.SlugRelatedField(
        read_only=True,
        slug_field= 'category'
     )

    class Meta:
        model = Shop
        fields = (
            'shop_id',
            'categoryid',
            'shop_name',
            'img',
            'phone',
            'openhour',
            'branch',
        )

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    shop = serializers.SlugRelatedField(
        read_only=True,
        slug_field='shop_name'
    )

    class Meta:
        model = Menu
        fields = (
            'menu_id',
            'shop',
            'menu_name',
            'extender_menu',
            'price',
        )

class LifeinfoSerializer(serializers.HyperlinkedModelSerializer):
    img = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )
    categoryid = serializers.SlugRelatedField(
        read_only=True,
        slug_field='category'
    )

    class Meta:
        model = Lifeinfo
        fields = (
            'categoryid',
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

class LifeinfoDetailListSerializer(serializers.HyperlinkedModelSerializer):
    img = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )
    categoryid = serializers.SlugRelatedField(
        read_only=True,
        slug_field='category'
    )
    class Meta:
        model = Lifeinfo
        fields = (
            'categoryid',
            'lifeinfoid',
            'lifeinfo_name',
            'branch',
            'phone',
            'openhour',
            'address',
            'address_url',
            'img',
            'category',
        )

class SearchSerializer(serializers.HyperlinkedModelSerializer):

    lifeinfo = LifeinfoSerializer(read_only=True)
    class Meta:
        model = Shop
        fields = (
            'shop_name',
            'branch',
            'phone',
            'img',
            'lifeinfo',
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