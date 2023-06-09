from django.db import models

# Create your models here.
class Posts(models.Model):
    class Meta:
        verbose_name = "Репосты"
        verbose_name_plural = "Репост"
        ordering = ["-created_at"]

    name = models.CharField(max_length=50, null=True, verbose_name = "Имя")
    image = models.ImageField(upload_to='media/image/%Y/%M/%D', verbose_name = "Изображение")
    text = models.TextField(max_length=300, null=True, verbose_name = "Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "Создан")
    update_at = models.DateTimeField(auto_now=True, verbose_name = "Обновлено")
    is_published = models.BooleanField(default=True, verbose_name = "Опубликован")

    def __str__(self):
        return self.name


class Music(models.Model):
    class Meta:
        verbose_name = "Музыка"
        verbose_name_plural = "Музыка"

    name = models.CharField(max_length=50, null=True, verbose_name = "Имя")
    track = models.FileField(upload_to='media/music/%Y/%M', verbose_name = "Файл музыки")
    name_abulm = models.ForeignKey('Abulm', on_delete=models.PROTECT, null=True, verbose_name = "Название альбома")
    name_band = models.ForeignKey('Bands', on_delete=models.PROTECT, null=True, verbose_name = "Название группы")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "Создан")
    update_at = models.DateTimeField(auto_now=True, verbose_name = "Обновлено")

    def __str__(self):
        return self.name


class Video(models.Model):
    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    name = models.CharField(max_length=50, null=True, verbose_name = "Имя")
    video = models.FileField(upload_to='media/video/%Y/%M/%D', verbose_name = "Файл видео")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "Создано")
    update_at = models.DateTimeField(auto_now=True, verbose_name = "Обновлено")

    def __str__(self):
        return self.name

    
class Bands(models.Model):
    class Meta:
        verbose_name = "Группы"
        verbose_name_plural = "Группа"

    name = models.CharField(max_length=50, null=True, verbose_name = "Название группы")
    image = models.ImageField(upload_to='media/image/%Y/%M/%D', verbose_name = "Изображение")

    def __str__(self):
        return self.name


class Abulm(models.Model):
    class Meta:
        verbose_name = "Альбомы"
        verbose_name_plural = "Альбом"

    name = models.CharField(max_length=50, null=True, verbose_name = "Название альбома")
    image = models.ImageField(upload_to='media/image/%Y/%M/%D', verbose_name = "Изображение")
    name_band = models.ForeignKey('Bands', on_delete=models.PROTECT, null=True, verbose_name = "Название группы")

    def __str__(self):
        return self.name
