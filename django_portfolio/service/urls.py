from django.urls import path, include
from .views import index, my_page, video, music, abulms

urlpatterns = [
    path('', index, name='index'),
    path('my_page/', my_page, name='my_page'),
    path('video/', video, name='video'),
    path('music/', music, name='music'),
    path('abulms/', abulms, name='abumls'),
]