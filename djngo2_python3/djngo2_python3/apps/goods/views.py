from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from goods.serializers import GoodsSerializer, GoodsPagination, CategorySerializer, BannerSerializer, IndexCategorySerializer, HotWordsSerializer
from .models import Goods, GoodsCategory, Banner,HotSearchWords
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


class GoodsListView(APIView):
    """
    商品列表
    """

    def get(self, request, format=None):
        goods = Goods.objects.all()
        goods_serialzer = GoodsSerializer(goods, many=True)
        return Response(goods_serialzer.data)

class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
    """
    商品列表
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

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
    list:
        商品列表，分页，搜索，过滤，排序

    retrieve:
        获取商品详情
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

    # 商品点击数
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class BannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    首页轮播图
    """
    queryset = Banner.objects.all().order_by("index")
    serializer_class = BannerSerializer

class IndexCategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    首页商品分类数据
    """
    # 获取is_tab = True(导航栏) 里面的分类下的商品数据
    queryset = GoodsCategory.objects.filter(is_tab=True, name__in=["啤酒"])
    serializer_class = IndexCategorySerializer

class HotSearchsViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取热搜词列表
    """
    queryset = HotSearchWords.objects.all().order_by("-index")
    serializer_class = HotWordsSerializer





