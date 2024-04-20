from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Названня товару')
    description = models.TextField(verbose_name='Опис')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Каталог')
    published_date = models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата публікації')
    contact = models.CharField(max_length=200, verbose_name='Контакти')
    STATUS_CHOICES = (
        ('active', 'Активно'),
        ('sold', 'Продано'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active', verbose_name='Статус')

    def __str__(self):
        return self.title
    
