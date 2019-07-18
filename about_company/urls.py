
from django.contrib import admin
from django.urls import path,include
from  .views import *
urlpatterns = [
    path('',My_details_views.as_view()),
]
