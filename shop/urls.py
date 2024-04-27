from django.urls import path
from .import views
app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('create/', views.create_product, name='create_product'),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('add_favorite/<int:product_id>/', views.add_favorite, name='add_favorite'),
    path('remove_favorite/<int:product_id>/', views.remove_favorite, name='remove_favorite'),
    path('favorites/', views.favorite_list, name='favorite_list'),
    path('my-products/', views.my_products, name='my_products'),
    path('reviews/', views.reviews, name='reviews'),
    path('add_review/', views.add_review, name='add_review'),
]