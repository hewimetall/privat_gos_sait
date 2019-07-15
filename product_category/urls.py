"""
URL Configuration
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .views import ArticleListView ,post_list
urlpatterns = [
    path('',post_list),
    path('<slug>',ArticleListView.as_view()),
]