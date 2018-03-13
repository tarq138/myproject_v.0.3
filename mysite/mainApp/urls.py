from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^100/', views.id1, name='id1'),
    url(r'^100-150/', views.id2, name='id2'),
    url(r'^150/', views.id3, name='id3'),
    url(r'^$', views.index, name='index'),
]
