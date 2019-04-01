# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     serializers
   Description :
   Author :       jusk?
   date：          2019/3/21
-------------------------------------------------
   Change Activity:
                   2019/3/21:
-------------------------------------------------
"""

from rest_framework import serializers
from user_operation.models import UserFav
from rest_framework.validators import UniqueTogetherValidator
from goods.serializers import GoodsSerializer
from .models import UserLeavingMessage, UserAddress

class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav

        # 使用validate方式实现唯一联合
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="已经收藏"
            )
        ]

        fields = ("user", "goods", "id")


class UserFavDetailSerializer(serializers.ModelSerializer):
    """
    用户收藏详情
    """

    # 通过商品id获取收藏的商品，需要嵌套商品的序列化
    goods = GoodsSerializer()
    class Meta:
        model = UserFav
        fields = ("goods", "id")

class LeavingMessageSerializer(serializers.ModelSerializer):
    """
    用户留言
    """
    # 获取当前登录的用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    # read_only: 只返回，post时候可以不用提交，format：格式化输出
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserLeavingMessage
        fields = ("user", "message_type", "subject", "message", "file", "id", "add_time")

class AddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserAddress
        fields = ("id", "user", "province", "city", "district", "address", "signer_name", "add_time", "signer_mobile")