from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from goods.serializers import GoodsSerializer
from .models import Goods
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
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

class GoodsPagination(PageNumberPagination):
    '''
    商品列表自定义分页
    '''
    #默认每页显示的个数
    page_size = 10
    #可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    #页码参数
    page_query_param = 'page'
    #最多能显示多少页
    max_page_size = 100

class GoodsListView(generics.ListAPIView):
    '商品列表页'
    pagination_class = GoodsPagination  # 分页
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


