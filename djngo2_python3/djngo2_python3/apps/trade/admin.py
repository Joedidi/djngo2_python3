from django.contrib import admin

# Register your models here.

import xadmin
from .models import ShoppingCart, OrderInfo, OrderGoods


class ShopingCartAdmin(object):
    list_display = ["user", "goods", "nums"]


class OrderInfoAdmin(object):
    list_display = ["user", "order_sn", "trade_no", "pay_status", "post_script",
                    "pay_time", "add_time"]

    class OrderGoodsInline(object):
        model = OrderGoods
        exclude = ["add_time", ]
        extra = 1
        style = 'tab'

    inlines = [OrderGoodsInline, ]

xadmin.site.register(ShoppingCart, ShopingCartAdmin)
xadmin.site.register(OrderInfo, OrderInfoAdmin)