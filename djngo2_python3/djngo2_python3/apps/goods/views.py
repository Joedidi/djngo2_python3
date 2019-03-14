from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from goods.serializers import GoodsSerializer
from .models import Goods
from rest_framework.response import Response

class GoodsListView(APIView):
    """
    商品列表
    """

    def get(self, request, format=None):
        goods = Goods.objects.all()
        goods_serialzer = GoodsSerializer(goods, many=True)
        return Response(goods_serialzer.data)
