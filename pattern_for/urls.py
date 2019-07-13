from django.urls import path
from .views import  *
from django.conf.urls import url

urlpatterns = [
    path('<reder>/',post_list),
    path('<cat>/<slug>/',post_titile,name='detail'),
]
