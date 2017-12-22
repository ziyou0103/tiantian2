from django.contrib import admin
from tt_goods.models import *


@admin.register(TypeGoods)
class TypeGoodsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'gtype', 'isDelete']


@admin.register(GoodsInfo)
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'gname', 'gpic', 'gprice', 'gunit', 'gclick', 'gjianjie', 'gkucun', 'gcontent', 'gtype', 'isDelete']

