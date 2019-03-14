# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     view_base
   Description :
   Author :       jusk?
   date：          2019/3/13
-------------------------------------------------
   Change Activity:
                   2019/3/13:
-------------------------------------------------
"""

# goods/view_base.py

from django.views.generic import View
from goods.models import Goods

class GoodsListView(View):
    def get(self,request):
        #通过django的view实现商品列表页
        json_list = []
        #获取所有商品
        goods = Goods.objects.all()
        for good in goods:
            json_dict = {}
            #获取商品的每个字段，键值对形式
            json_dict['name'] = good.name
            json_dict['category'] = good.category.name
            json_dict['market_price'] = good.market_price
            json_list.append(json_dict)

        from django.http import HttpResponse
        import json
        #返回json，一定要指定类型content_type='application/json'
        return HttpResponse(json.dumps(json_list),content_type='application/json')