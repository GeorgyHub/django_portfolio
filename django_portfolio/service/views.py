from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView, CreateView
from .models import Posts, Bands, Video, Music, Abulm
from .forms import PostsForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def index(request):
    posts = Posts.objects.all()
    bands = Bands.objects.all()
    video = Video.objects.all()
    music = Music.objects.all()
    abulm = Abulm.objects.all()
    return render(request, 'service/index.html', {'title': 'Новости', 'posts': posts})

def sing_up(request):
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            messages.sucess(request, 'Регистрация прошла успешно')
            return redirect('sing_in')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserCreationForm()
    return render(request, 'service/sing_up.html', {'title': 'Зарегистрироваться', 'form': form})

def sing_in(request):
    return render(request, 'service/sing_in.html', {'title': 'Войти'})

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
    return render(request, 'service/music.html', {'title': 'Музыка', 'bands': bands, 'music': music, 'abulm': abulm, 'video': video})

def video(request):
    posts = Posts.objects.all()
    bands = Bands.objects.all()
    video = Video.objects.all()
    music = Music.objects.all()
    abulm = Abulm.objects.all()
    return render(request, 'service/video.html', {'title': 'Видео', 'video': video})

def abulms(request, abulm_id, music_id, band_id):
    posts = Posts.objects.all()
    bands = Bands.objects.all()
    video = Video.objects.all()
    music = Music.objects.all(abulm_id=abulm_id)
    abulm = Abulm.objects.all()
    return render(request, 'service/music/abulms.html', {'title': 'Музыкальные альбомы', 
                                                    'bands': bands, 
                                                    'music': music, 
                                                    'abulm': abulm})
    
def add_post(request):
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            posts = Posts.objects.create(**form.creaned_data)
            return redirect(posts)
    else:
        form = PostsForm
    return render(request, 'service/add_post.html', {'title': 'Добавить запись', 'form': form})

