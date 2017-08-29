# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
            'category',
            'shop_or_lifeinfo',
            'img',
        )

class ShopAdmin(admin.ModelAdmin):
    model = Shop
    list_display = (
            'shop_id',
            'shop_name',
            'category_name_view',
            'img',
            'branch',
            'phone',
            'openhour',
        )
    search_fields = ('shop_name',)

    def category_name_view(self, obj):
        return obj.categoryid.category

    raw_id_fields = ("categoryid",)

class LifeinfoAdmin(admin.ModelAdmin):
    list_display = (
            'lifeinfo_name',
            'category_name_view',
            'img',
            'branch',
            'phone',
            'openhour',
            'address',
            'address_url',
        )
    search_fields = ('lifeinfo_name',)

    def category_name_view(self, obj):
        return obj.categoryid.category

    raw_id_fields = ("categoryid",)

class MenuAdmin(admin.ModelAdmin):
    list_display = (
            'shop_name_view',
            'menu_name',
            'extender_menu',
            'price',
        )
    search_fields = ('menu_name',)

    def shop_name_view(self, obj):
        return obj.shop.shop_name

    raw_id_fields = ("shop",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Lifeinfo, LifeinfoAdmin)
admin.site.register(Menu, MenuAdmin)