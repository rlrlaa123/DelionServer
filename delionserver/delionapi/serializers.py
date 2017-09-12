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
#
class ShopLifeinfoSerializer(serializers.HyperlinkedModelSerializer):
    img = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field= 'category'
     )

    class Meta:
        model = ShopLifeinfo
        fields = (
            'shop_lifeinfo_id',
            'category',
            'name',
            'img',
            'phone',
            'openhour',
            'branch',
            'address',
            'address_url',
        )

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    shop = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
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

class SearchSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ShopLifeinfo
        fields = (
            'shop_lifeinfo_id',
            'name',
            'branch',
            'phone',
        )