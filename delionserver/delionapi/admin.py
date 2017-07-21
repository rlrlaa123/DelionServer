# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from delionapi.models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
            'category',
            'shop_or_lifeinfo',
        )

class ShopAdmin(admin.ModelAdmin):
    model = Shop
    list_display = (
            'category',
            'shop_name',
            'img',
            'branch',
            'phone',
            'openhour',
        )
    search_fields = ('shop_name',)

class LifeInfoAdmin(admin.ModelAdmin):
    list_display = (
            'category',
            'lifeinfo_name',
            'img',
            'branch',
            'phone',
            'openhour',
            'address',
            'address_url',
        )

class MenuAdmin(admin.ModelAdmin):
    list_display = (
            'shop_name_view',
            'menu_name',
            'extender_menu',
            'price',
        )
    def shop_name_view(self, obj):
        return obj.shop_name.shop_name

    raw_id_fields = ("shop_name",)

class CsvAdmin(admin.ModelAdmin):
    list_display = (
            'csv',
        )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(LifeInfo, LifeInfoAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Csv, CsvAdmin)