from django.conf.urls import url
from . import views
from django.urls import path


app_name="cart"

urlpatterns = [
    path('remove/for/<product_id>/', views.CartRemove_for, name='CartRemove_for'),
    path('add/for/<product_id>/', views.CartAdd_for, name='CartAdd_for'),
    url(r'^$', views.CartDetail, name='CartDetail'),
    url(r'^remove/(?P<product_id>\d+)/$', views.CartRemove, name='CartRemove'),
    url(r'^add/(?P<product_id>\d+)/$', views.CartAdd, name='CartAdd'),
]
