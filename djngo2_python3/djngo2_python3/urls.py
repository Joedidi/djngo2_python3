"""djngo2_python3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
import xadmin
from django.views.static import serve
from djngo2_python3.settings import MEDIA_ROOT
# from goods.view_base import GoodsListView
from goods.views import GoodsListView
from rest_framework.documentation import include_docs_urls
from goods.views import GoodsListViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from users.views import SmsCodeViewset, UserViewset
router = DefaultRouter()
#配置goods的url
router.register(r'goods', GoodsListViewSet)
#配置code的url
router.register(r'code', SmsCodeViewset, base_name="code")
#配置用户的url
router.register(r'users', UserViewset , base_name="users")

# 配置Category的url
router.register(r'categorys', CategoryViewSet, base_name="categorys")
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    #文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),

    # path('goods/', GoodsListView.as_view(), name='goods-list'),

    # drf 文档，title自定义
    path('docs/', include_docs_urls(title='杭州立幼网络科技有限公司')),

    path('api-auth/', include('rest_framework.urls')),

    re_path('^', include(router.urls)),

    # token
    path('api-token-auth/', views.obtain_auth_token),

    # jwt的token认证接口
    path('api-token-auth/', obtain_jwt_token),
    # jwt的认证接口
    path('login/', obtain_jwt_token)
]

