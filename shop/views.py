from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductForm

def index(request):
    return render(request, 'shop/index.html')

def product_list(request):
    categories = Category.objects.all().prefetch_related('product_set')
    return render(request, 'shop/product_list.html', {'categories': categories})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'shop/product_detail.html', {'product': product})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:product_list')
    else:
        form = ProductForm()
    return render(request, 'shop/create_product.html', {'form': form})