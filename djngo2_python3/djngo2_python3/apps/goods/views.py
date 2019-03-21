from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from goods.serializers import GoodsSerializer,GoodsPagination, CategorySerializer
from .models import Goods,GoodsCategory
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
import django_filters
from .filters import GoodsFilter
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from rest_framework_extensions.cache.mixins import CacheResponseMixin


# class GoodsListView(APIView):
#     """
#     商品列表
#     """
#
#     def get(self, request, format=None):
#         goods = Goods.objects.all()
#         goods_serialzer = GoodsSerializer(goods, many=True)
#         return Response(goods_serialzer.data)

# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
#     """
#     商品列表
#     """
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

class GoodsListView(generics.ListAPIView):
    '商品列表页'
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)



class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    """
    商品列表，分页，搜索，过滤，排序
    """
    queryset = Goods.objects.all()
    # 序列化
    serializer_class = GoodsSerializer
    # 分页
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('name', 'shop_price')
    # 过滤
    filter_class = GoodsFilter
    # 搜索
    search_fields = ('name', 'goods_brief', 'goods_desc')
    # 排序
    ordering_fields = ('sold_num', 'shop_price')






