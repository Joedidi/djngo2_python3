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
from .models import Goods, GoodsCategory, GoodsImage, Banner, IndexAd, HotSearchWords
from rest_framework.pagination import PageNumberPagination

from django.db.models import Q

# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


# 商品轮播图
class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ('image',)
        # fields = '__all__'

#商品列表页
class GoodsSerializer(serializers.ModelSerializer):
    #覆盖外键字段
    category_name = CategorySerializer()
    #images是数据库中设置的related_name="images"，把轮播图嵌套进来
    images = GoodsImageSerializer(many=True)
    class Meta:
        model = Goods
        fields = "__all__"



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

class BannerSerializer(serializers.ModelSerializer):
    """
    轮播图
    """
    class Meta:
        model = Banner
        fields = "__all__"

class BrandSerializer(serializers.ModelSerializer):
    """
    大类下面的宣传商标
    """
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class IndexCategorySerializer(serializers.ModelSerializer):
    #某个大类的商标，可以有多个商标，一对多的关系
    brands = BrandSerializer(many=True)
    # good有一个外键category，但这个外键指向的是三级类，直接反向通过外键category（三级类），取某个大类下面的商品是取不出来的
    goods = serializers.SerializerMethodField()
    # 在parent_category字段中定义的related_name="sub_cat"
    # 取二级商品分类
    sub_cat = CategorySerializer2(many=True)
    # 广告商品
    ad_goods = serializers.SerializerMethodField()

    def get_ad_goods(self, obj):
        goods_json = {}
        ad_goods = IndexAd.objects.filter(category_id=obj.id, )
        if ad_goods:
            #取到这个商品Queryset[0]
            good_ins = ad_goods[0].goods
            #在serializer里面调用serializer的话，就要添加一个参数context（上下文request）,嵌套serializer必须加
            # serializer返回的时候一定要加 “.data” ，这样才是json数据
            goods_json = GoodsSerializer(good_ins, many=False, context={'request': self.context['request']}).data
        return goods_json

    #自定义获取方法
    def get_goods(self, obj):
        # 将这个商品相关父类子类等都可以进行匹配
        all_goods = Goods.objects.filter(Q(category_id=obj.id) | Q(category__parent_category_id=obj.id) | Q(
            category__parent_category__parent_category_id=obj.id))
        goods_serializer = GoodsSerializer(all_goods, many=True, context={'request': self.context['request']})
        return goods_serializer.data

    class Meta:
        model = GoodsCategory
        fields = "__all__"

class HotWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotSearchWords
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

