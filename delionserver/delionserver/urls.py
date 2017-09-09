"""delionserver URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from delionapi import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^category/$', views.CategoryList.as_view()),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
    url(r'^shop/$', views.ShopList.as_view()),
    url(r'^shop/(?P<pk>[0-9]+)/$', views.ShopDetail.as_view()),
    url(r'^shop/menu/$', views.MenuList.as_view()),
    url(r'^shop/menu/(?P<pk>[0-9]+)/$', views.MenuDetail.as_view()),
    url(r'^lifeinfo/$', views.LifeinfoList.as_view()),
    url(r'^lifeinfo/detail/$', views.LifeinfoDetailList.as_view()),
    url(r'^lifeinfo/(?P<pk>[0-9]+)/$', views.LifeinfoDetail.as_view()),
    url(r'^search/$', views.SearchList.as_view(), name="search"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]