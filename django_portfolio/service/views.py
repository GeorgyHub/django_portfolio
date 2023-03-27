from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts, Bands, Video, Music, Abulm

# Create your views here.
def index(request):
    posts = Posts.objects.all()
    bands = Bands.objects.all()
    video = Video.objects.all()
    music = Music.objects.all()
    abulm = Abulm.objects.all()
    return render(request, 'service/index.html', {'title': 'Новости'})

def my_page(request):
    posts = Posts.objects.all()
    bands = Bands.objects.all()
    video = Video.objects.all()
    music = Music.objects.all()
    abulm = Abulm.objects.all()
    return render(request, 'service/my_page.html')

def music(request):
    posts = Posts.objects.all()
    bands = Bands.objects.all()
    video = Video.objects.all()
    music = Music.objects.all()
    abulm = Abulm.objects.all()
    return render(request, 'service/music.html', {'title': 'Музыка'})

def video(request):
    posts = Posts.objects.all()
    bands = Bands.objects.all()
    video = Video.objects.all()
    music = Music.objects.all()
    abulm = Abulm.objects.all()
    return render(request, 'service/video.html', {'title': 'Видео'})

def abulms(request):
    posts = Posts.objects.all()
    bands = Bands.objects.all()
    video = Video.objects.all()
    music = Music.objects.all()
    abulm = Abulm.objects.all()
    return render(request, 'service/abulms.html', {'title': 'Музыкальные альбомы'})