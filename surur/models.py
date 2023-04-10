from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Заголовок')
    image = models.FileField(upload_to='category_photo/', verbose_name='Изображение категории')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tour(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    image1 = models.ImageField(upload_to='photo_tour/', verbose_name='Фото Тура', null=True)
    image2 = models.ImageField(upload_to='photo_tour/', verbose_name='Фото Тура', null=True)
    image3 = models.ImageField(upload_to='photo_tour/', verbose_name='Фото Тура', null=True)
    image4 = models.ImageField(upload_to='photo_tour/', verbose_name='Фото Тура', null=True)
    watched = models.IntegerField(default=True, verbose_name='Просмотры')
    price = models.FloatField(default=0, verbose_name='Цена')
