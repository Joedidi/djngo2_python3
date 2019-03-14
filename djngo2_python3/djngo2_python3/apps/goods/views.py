from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from goods.serializers import GoodsSerializer,GoodsPagination
from .models import Goods
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


class GoodsListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    商品列表页，分页，搜索，过滤，排序,取某一个具体商品的详情
    """

    # queryset是一个属性
    # good_viewset.queryset就可以访问到
    # 函数就必须调用good_viewset.get_queryset()函数
    # 如果有了下面的get_queryset。那么上面的这个就不需要了。
    # queryset = Goods.objects.all()

    throttle_classes = (UserRateThrottle, AnonRateThrottle)
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    queryset = Goods.objects.all()

    # 设置列表页的单独auth认证也就是不认证
    # authentication_classes = (TokenAuthentication,)

    # 设置三大常用过滤器之DjangoFilterBackend, SearchFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 设置排序
    ordering_fields = ('sold_num', 'shop_price')
    # 设置filter的类为我们自定义的类
    filter_class = GoodsFilter

    # 设置我们的search字段
    search_fields = ('name', 'goods_brief', 'goods_desc')



