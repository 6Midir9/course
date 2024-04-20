from django.shortcuts import render, redirect, get_object_or_404
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
    
    context = {'form': form}
    return render(request, 'shop/create_product.html', context)

def edit_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('shop:product_detail', id=product.id)
    else:
        form = ProductForm(instance=product)

    context = {'form': form, 'product': product}
    return render(request, 'shop/edit_product.html', context)

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('shop:product_list')
    
    context = {'product': product}
    return render(request, 'shop/delete_product.html', context)