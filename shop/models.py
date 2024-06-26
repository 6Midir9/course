from django.db import models
import datetime
from django.conf import settings

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
    created_at = models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата публікації')
    contact = models.CharField(max_length=200, verbose_name='Контакти')
    location = models.CharField(max_length=400, verbose_name='Місцезнаходження')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(blank=True, upload_to='images', verbose_name='Зображення')
    
    def __str__(self):
        return self.title
    
class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="favorites")
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="favorited_by")

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return self.user.username
    
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField(default=5, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Оцінка')
    comment = models.TextField(verbose_name='Відгук')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.created_at.strftime('%Y-%m-%d')}"