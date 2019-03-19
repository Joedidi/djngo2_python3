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
from rest_framework.pagination import PageNumberPagination

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



class CategorySerializer3(serializers.ModelSerializer):
    """三级分类"""
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class CategorySerializer2(serializers.ModelSerializer):
    """
    二级分类
    """
    # 在parent_category 字段中定义的related_name = "sub_cat"
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    """
    商品一级类别序列化
    """
    sub_cat = CategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


    

class GoodsPagination(PageNumberPagination):
    """
    商品列表自定义分页
    """

    # 默认煤业显示的个数
    page_size = 12
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 100

