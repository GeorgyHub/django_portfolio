from django.urls import path
from .views import index, sing_in, sing_up, my_page, video, music, abulms, add_post


urlpatterns = [
    path('', index, name='index'),
    path('add_post/', add_post, name='add_post'),
    path('sing_in', sing_in, name='sing_in'),
    path('sing_up', sing_up, name='sing_up'),
    path('my_page/', my_page, name='my_page'),
    path('video/', video, name='video'),
    path('music/', music, name='music'),
    path('abulm/', abulms, name='abuml'),
]

