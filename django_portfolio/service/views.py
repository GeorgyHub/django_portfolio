from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts, Bands, Video, Music, Abulm

# Create your views here.
def index(request):
    posts = Posts.objects.all()
    return render(request, 'service/index.html', {'title': 'Главная'})

def music(request):
    return render(request, 'service/music.html', {'title': 'Музыка'})

def video(request):
    return render(request, 'service/video.html', {'title': 'Видео'})

def abulms(request):
    return render(request, 'service/abulms.html', {'title': 'Музыкальные альбомы'})