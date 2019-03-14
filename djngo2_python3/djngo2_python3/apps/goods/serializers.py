# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     serializers
   Description :
   Author :       jusk?
   date：          2019/3/14
-------------------------------------------------
   Change Activity:
                   2019/3/14:
-------------------------------------------------
"""

from rest_framework import serializers
from .models import Goods, GoodsCategory


# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


#　ModelSerializer实现商品列表页
class GoodsSerializer(serializers.ModelSerializer):
    category_name = CategorySerializer()
    class Meta:
        model = Goods
        fields = '__all__'


