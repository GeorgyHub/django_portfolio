from django.contrib import admin
from .models import Posts, Bands, Video, Music, Abulm

# Register your models here.


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'text', 'created_at', 'update_at', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

class BandsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'video', 'created_at', 'update_at')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

class MusicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'track', 'name_abulm', 'name_band', 'created_at', 'update_at')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'name_band')

class AbulmAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'name_band')
    list_display_links = ('id', 'name', 'name_band')
    search_fields = ('id', 'name', 'name_band')


admin.site.register(Posts, PostsAdmin)
admin.site.register(Bands, BandsAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Music, MusicAdmin)
admin.site.register(Abulm, AbulmAdmin)