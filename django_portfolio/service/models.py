from django.db import models

# Create your models here.
class Posts(models.Model):
    class Meta:
        verbose_name = "Репосты"
        verbose_name_plural = "Репост"
        ordering = ["-created_at"]

    name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='media/image/%Y/%M/%D')
    text = models.TextField(max_length=300, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


class Music(models.Model):
    class Meta:
        verbose_name = "Музыка"
        verbose_name_plural = "Музыка"

    name = models.CharField(max_length=50, null=True)
    track = models.FileField(upload_to='media/music/%Y/%M/%D')
    name_band = models.ForeignKey('Bands', on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Video(models.Model):
    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    name = models.CharField(max_length=50, null=True)
    video = models.FileField(upload_to='media/video/%Y/%M/%D')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    
class Bands(models.Model):
    class Meta:
        verbose_name = "Группы"
        verbose_name_plural = "Группа"

    name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='media/image/%Y/%M/%D')


class Abulm(models.Model):
    class Meta:
        verbose_name = "Альбомы"
        verbose_name_plural = "Альбом"

    name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='media/image/%Y/%M/%D')
    name_band = models.ForeignKey('Bands', on_delete=models.PROTECT, null=True)
