from django.contrib import admin

# Register your models here.

import xadmin
from .models import Goods, GoodsCategory, GoodsImage, GoodsCategoryBrand, Banner, HotSearchWords
from .models import IndexAd


class GoodsAdmin(object):
    # 显示的列
    list_display = ["name", "clicks_num", "sold_num", "fav_num", "goods_num", "market_price",
                    "shop", "goods_brief", "goods_desc", "is_new", "is_hot", "add_time"]

    # 可以搜索的字段
    search_fields = ['name',]
    # list_editable = ["is_hot",]
    # 过滤器
    list_filter = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                   "shop_price", "is_new", "is_hot", "add_time", "category_name"]

    # 富文本编辑器
    style_fields = {"doods_desc": "ueditor"}

    # 在添加商品的时候可以添加商品图片
    class GoodsImagesInline(object):
        model = GoodsImage
        exclude = ["add_time"]
        extra = 1
        style = 'tab'

    inlines = [GoodsImagesInline]

class GoodsCategoryAdmin(object):
    list_display = ["name", "category_type", "parent_category", "add_time"]
    list_filter = ["category", "parent_category", "name"]
    search_fields = ["name"]


class GoodsBrandAdmin(object):
    list_display = ["category", "image", "name", "desc"]

    def get_context(self):
        context = super(GoodsBrandAdmin, self).get_context()
        if 'form' in context:
            context['form'].fields['category'].queryset = GoodsCategory.objects.filter(category_type=1)
        return context


class BannerGoodsAdmin(object):
    list_display = ["goods", "image", "index"]

class HotSearchAdmin(object):
    list_display = ["keywords", "index", "add_time"]

class IndexAdmin(object):
    list_display = ["category", "goods"]

xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(Banner, BannerGoodsAdmin)
xadmin.site.register(GoodsCategoryBrand, GoodsBrandAdmin)


xadmin.site.register(HotSearchWords, HotSearchAdmin)
xadmin.site.register(IndexAd, IndexAdmin)