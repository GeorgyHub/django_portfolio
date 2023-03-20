from django.urls import path, include
from .views import index, video, music, abulms

urlpatterns = [
    path('', index, name='index'),
    path('video/', video, name='video'),
    path('music/', music, name='music'),
    path('abulms/', abulms, name='abumls'),
]