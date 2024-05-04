from django import forms
from .models import Product, Review, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'created_at', 'contact', 'location', 'category', 'image']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

class CategoryFilterForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, label='Категорія')
    query = forms.CharField(max_length=100, required=False, label='Пошук')