from django import forms
from django.forms import ModelForm
from .models import Posts, Video, Bands, Abulm, Music
import re
from django.core.exceptions import ValidationError


class PostsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Заголовок', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content = forms.CharField(label='Опишите вашу запись',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows':5})
    )
    image = forms.ImageField(label='Изображение', initial=True)
    is_published = forms.BooleanField(label='Опубликовать')


    