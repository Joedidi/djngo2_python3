from django.db import models

# Create your models here.


from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    用户信息
    """
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )
    #用户用手机注册，所以姓名，生日和邮箱可以为空
    name = models.CharField("姓名",max_length=30, null=True, blank=True, help_text="姓名")
    birthday = models.DateField("出生年月",null=True, blank=True, help_text="出生年月")
    gender = models.CharField("性别",max_length=6, choices=GENDER_CHOICES, default="female", help_text="性别")
    mobile = models.CharField("电话", max_length=11, null=True, blank=True, help_text="电话")
    email = models.EmailField("邮箱",max_length=100, null=True, blank=True, help_text="邮箱")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    验证码
    """
    code = models.CharField("验证码", max_length=10, help_text="验证码")
    mobile = models.CharField("电话", max_length=11, null=True, blank=True, help_text="电话")
    add_time = models.DateTimeField("添加时间", default=datetime.now, help_text="添加时间")

    class Meta:
        verbose_name = "短信验证"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


# 访问网站的ip地址，端点和次数
class UserIP(models.Model):
    ip = models.CharField(verbose_name='IP 地址', max_length=30, help_text="ip地址")
    ip_addr = models.CharField(verbose_name='IP 地理位置', max_length=30, help_text="ip地理位置")
    end_point = models.CharField(verbose_name='访问端点', default='/', max_length=30, help_text="访问端点")
    count = models.IntegerField(verbose_name="访问次数", default=0, help_text="访问次数")

    class Meta:
        verbose_name = "访问用户信息"
        verbose_name_plural = verbose_name

# 网站总访问次数
class VisitNumber(models.Model):
    count = models.IntegerField(verbose_name='网站访问总次数', default=0, help_text="网站访问总次数")

    class Meta:
        verbose_name = '网站访问总次数'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.count)

# 单日访问统计
class DayNumber(models.Model):
    day = models.DateTimeField(verbose_name='日期', default=datetime.now, help_text="日期")
    count = models.IntegerField(verbose_name='网站访问次数', default=0)       # 网站访问总次数

    class Meta:
        verbose_name = "网站日访问统计"
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.day)

