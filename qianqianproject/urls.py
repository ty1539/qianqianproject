"""qianqianproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import xadmin

from qianqianproject.settings import MEDIA_ROOT
from rest_framework_jwt.views import obtain_jwt_token
from django.views.static import serve
from rest_framework.documentation import include_docs_urls

from activity.urls import urlpatterns as activityurl
from discount_coupon.urls import urlpatterns as discount_couponurl
from points_mall.urls import urlpatterns as points_mallurl
from order.urls import urlpatterns as orderurl
from store.urls import urlpatterns as storeurl
from users.urls import urlpatterns as usersurl

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^admin/', admin.site.urls),
    url(r'authorizations/', obtain_jwt_token, name='authorizations'),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),  # 设置media 路径
    url(r'^docs/', include_docs_urls(title='My API title')),
    url(r'xadmin/', include(xadmin.site.urls)),
    url(r'^ueditor/', include('DjangoUeditor.urls')),

    url(r'^', include((usersurl, "users"), namespace="users")),
    url(r'^', include((activityurl, "activity"), namespace="activity")),
    url(r'^', include((discount_couponurl, "discount_coupon"), namespace="discount_coupon")),
    url(r'^', include((orderurl, "order"), namespace="order")),
    url(r'^', include((points_mallurl, "points_mall"), namespace="points_mall")),
    url(r'^', include((storeurl, "store"), namespace="store")),

]
