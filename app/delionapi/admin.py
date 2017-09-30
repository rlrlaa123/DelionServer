# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
            'category_id',
            'category',
            'shop_or_lifeinfo',
            'img',
        )

class ShopLifeinfoAdmin(admin.ModelAdmin):
    model = ShopLifeinfo
    list_display = (
            'shop_lifeinfo_id',
            'name',
            'category_name_view',
            'img',
            'branch',
            'phone',
            'openhour',
            'address',
            'address_url',
        )
    search_fields = ('name',)

    def category_name_view(self, obj):
        return obj.category.category

    raw_id_fields = ("category",)

class MenuAdmin(admin.ModelAdmin):
    list_display = (
            'menu_id',
            'shop_name_view',
            'menu_name',
            'extender_menu',
            'price',
        )
    search_fields = ('menu_name',)

    def shop_name_view(self, obj):
        return obj.shop.name

    raw_id_fields = ("shop",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(ShopLifeinfo, ShopLifeinfoAdmin)
admin.site.register(Menu, MenuAdmin)