from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^newlogo.png', views.index, name='index'),
]
