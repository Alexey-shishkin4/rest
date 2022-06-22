from django.db import models
import django
from random import sample
from django.db.models.aggregates import Count
from sorl.thumbnail import get_thumbnail, ImageField
from django.utils.safestring import mark_safe
from datetime import datetime

class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Dish(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    calories = models.CharField(verbose_name='Каллорийность', max_length=100, blank=True)
    weight = models.CharField(verbose_name='Масса', max_length=100, blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2)
    compound = models.TextField(verbose_name='Состав', max_length=250, blank=True)
    upload = ImageField(default=None, upload_to='uploads/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def get_image_250x250(self):
        return get_thumbnail(self.upload, '250x250', crop='center', quality=51)

    def get_image_400x300(self):
        return get_thumbnail(self.upload, '400x300', crop='center', quality=51)
    
    def get_image_1024x1280(self):
        return get_thumbnail(self.upload, '1024x1280', crop='center', quality=102)

    def img_tmb(self):
        return mark_safe(f'<img src="{self.upload.url}" width="50">') if self.upload else 'Нет изображений'

    img_tmb.short_description = 'превью'
    img_tmb.allow_tags = True

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'


class Gallery(models.Model):
    item_image = models.ImageField(upload_to="uploads/", blank=True)
    item = models.ForeignKey(Dish, on_delete=models.PROTECT, verbose_name="Блюдо", default=None)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def get_image_400x300(self):
        return get_thumbnail(self.item_image, '400x300', crop='center', quality=51)
    
    def img_tmb(self):
        return mark_safe(f'<img src="{self.item_image.url}" width="50">') if self.item_image else 'Нет изображений'


class ImagesManager(models.Manager):
    def random3(self):
        count = self.aggregate(count=Count('id'))['count']
        indesex = list(range(0, count))
        random_index = sample(indesex, k=3)
        sp = []
        for i in random_index:
            sp.append(self.all()[i])
        return sp
    
    def random6(self):
        count = self.aggregate(count=Count('id'))['count']
        indesex = list(range(0, count))
        random_index = sample(indesex, k=6)
        sp = []
        for i in random_index:
            sp.append(self.all()[i])
        return sp


class Images(models.Model):
    objects = ImagesManager()

    image = models.ImageField(upload_to="uploads/", blank=True)

    class Meta:
        verbose_name = "Галлерея"
        verbose_name_plural = "Галлерея"

    def get_image_400x300(self):
        return get_thumbnail(self.image, '400x300', crop='center', quality=51)
    
    def get_image_1024x1280(self):
        return get_thumbnail(self.image, '1024x1280', crop='center', quality=102)
    
    def img_tmb(self):
        return mark_safe(f'<img src="{self.image.url}" width="50">') if self.image else 'Нет изображений'


class News(models.Model):
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    image = models.ImageField(upload_to="uploads/")
    title = models.CharField(max_length=200, verbose_name='Название')
    text = models.TextField(max_length=500, verbose_name='Текст')
    when = models.CharField(max_length=100, verbose_name='Когда', blank=False, default=datetime.now())
    entrance = models.CharField(max_length=200, verbose_name='Дополнительная информация по входу', blank=True)
    published_date = models.DateTimeField(verbose_name="Дата публикации", default=datetime.now())
    
    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
    
    def get_image_400x300(self):
        return get_thumbnail(self.image, '400x300', crop='center', quality=51)
    
    def get_image_1024x1280(self):
        return get_thumbnail(self.image, '1024x1280', crop='center', quality=102)
    
    def img_tmb(self):
        return mark_safe(f'<img src="{self.image.url}" width="50">') if self.image else 'Нет изображений'
