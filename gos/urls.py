"""gos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('users/', admin.site.urls),
    path('',include('about_company.urls'),name="root"),
    path('art/',include('pattern_for.urls')),
    url(r'^markdownx/', include('markdownx.urls')),
    path('forma_obratnoj_svyazi/', include('forma_obratnoj_svyazi.urls')),
    path('mag/', include('product_category.urls')),
    path('news/', include('blog.urls')),
    path('cart/', include('cart.urls',namespace='cart')),
   path('admin_tools/', include('admin_tools.urls')),
    path('mdeditor/',include('mdeditor.urls')),

   ]
