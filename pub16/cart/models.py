from django.db import models
from datetime import datetime


class Orders(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    email = models.EmailField(verbose_name='Почта', max_length=100)
    addres = models.CharField(verbose_name='Адрес', max_length=200)
    phone = models.CharField(verbose_name='Телефон', max_length=30)
    date = models.DateTimeField(verbose_name='Дата',  default=datetime.now(), blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
