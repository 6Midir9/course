from django.urls import path
from .import views
app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('create/', views.create_product, name='create_product'),
]