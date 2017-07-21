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
from delionserver import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^category/$', views.CategoryList.as_view()),
    url(r'^shop/$', views.ShopList.as_view()),
    url(r'^lifeinfo/$', views.LifeInfoList.as_view()),
    url(r'^menu/$', views.MenuList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static('/upload_files/',document_root=settings.MEDIA_ROOT)
#media file을 제공하는 url패턴