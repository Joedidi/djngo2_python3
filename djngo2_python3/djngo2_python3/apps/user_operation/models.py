from django.db import models
from datetime import datetime
from  goods.models import Goods


from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class UserFav(models.Model):
    """
    用户收藏操作
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户", help_text="用户")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品", help_text="商品id")
    add_time = models.DateTimeField("添加时间", default=datetime.now, help_text="添加时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return self.user.username


class UserAddress(models.Model):
    """
    用户收货地址
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户", help_text="用户")
    province = models.CharField("省份", max_length=100, default="", help_text="省份")
    city = models.CharField("城市", max_length=100, default="", help_text="城市")
    district = models.CharField("区域", max_length=100, default="", help_text="区域")
    address = models.CharField("详细地址", max_length=100, default="", help_text="详细地址")
    signer_name = models.CharField("签收人", max_length=100, default="", help_text="签收人")
    signer_mobile = models.CharField("电话", max_length=11, default="", help_text="电话")
    add_time = models.DateTimeField("添加时间", default=datetime.now, help_text="添加时间")

    class Meta:
        verbose_name = "收货地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address

class UserLeavingMessage(models.Model):
    """
    用户留言
    """

    MESSAGE_CHICES = (
        (1, "留言"),
        (2, "投诉"),
        (3, "询问"),
        (4, "售后"),
        (5, "求购"),

    )


    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户", help_text="用户")
    message_type = models.BigIntegerField(default=1, choices=MESSAGE_CHICES, verbose_name="留言类型", help_text=u"留言类型:1(留言), 2(投诉), 3(询问), 4(售后), 5(求购)")
    subject = models.CharField("主题", max_length=100, default="", help_text="主题")
    message = models.TextField("留言内同", default="", help_text="留言内容")
    file = models.FileField(upload_to="message/images/", verbose_name="上传的文件", help_text="上传的文件")

    add_time = models.DateTimeField("添加时间", default=datetime.now, help_text="添加时间")

    class Meta:
        verbose_name="用户留言"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


