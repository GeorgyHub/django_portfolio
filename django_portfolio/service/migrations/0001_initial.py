# Generated by Django 4.1.7 on 2023-03-27 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Название группы')),
                ('image', models.ImageField(upload_to='media/image/%Y/%M/%D', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Группы',
                'verbose_name_plural': 'Группа',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Имя')),
                ('image', models.ImageField(upload_to='media/image/%Y/%M/%D', verbose_name='Изображение')),
                ('text', models.TextField(max_length=300, null=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликован')),
            ],
            options={
                'verbose_name': 'Репосты',
                'verbose_name_plural': 'Репост',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Имя')),
                ('video', models.FileField(upload_to='media/video/%Y/%M/%D', verbose_name='Файл видео')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Имя')),
                ('track', models.FileField(upload_to='media/music/%Y/%M/%D', verbose_name='Файл музыки')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('name_band', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='service.bands', verbose_name='Название группы')),
            ],
            options={
                'verbose_name': 'Музыка',
                'verbose_name_plural': 'Музыка',
            },
        ),
        migrations.CreateModel(
            name='Abulm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Название альбома')),
                ('image', models.ImageField(upload_to='media/image/%Y/%M/%D', verbose_name='Изображение')),
                ('name_band', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='service.bands', verbose_name='Название группы')),
            ],
            options={
                'verbose_name': 'Альбомы',
                'verbose_name_plural': 'Альбом',
            },
        ),
    ]
