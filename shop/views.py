from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Favorite, Review
from .forms import ProductForm, ReviewForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'shop/index.html')

@login_required
def product_list(request):
    categories = Category.objects.all()
    return render(request, 'shop/product_list.html', {'categories': categories})

@login_required
def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'shop/product_detail.html', {'product': product})

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
           product = form.save(commit=False)
           product.owner = request.user
           product.save()
        return redirect('shop:product_detail', id=product.id)
    else:
        form = ProductForm()
    
    context = {'form': form}
    return render(request, 'shop/create_product.html', context)

@login_required
def edit_product(request, id):
    product = Product.objects.get(id=id)
    if request.user != product.owner and not request.user.is_superuser:
        return redirect('shop:product_list')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('shop:product_detail', id=product.id)
    else:
        form = ProductForm(instance=product)

    context = {'form': form, 'product': product}
    return render(request, 'shop/edit_product.html', context)

@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.user != product.owner and not request.user.is_superuser:
        return redirect('shop:product_list')
    if request.method == 'POST':
        product.delete()
        return redirect('shop:product_list')
    
    context = {'product': product}
    return render(request, 'shop/delete_product.html', context)

@login_required
def add_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Favorite.objects.get_or_create(user=request.user, product=product)
    return redirect('shop:product_detail', id=product_id)

@login_required
def remove_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Favorite.objects.filter(user=request.user, product=product).delete()
    return redirect('shop:favorite_list')

@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('product')
    return render(request, 'shop/favorite_list.html', {'favorites': favorites})

@login_required
def my_products(request):
    products = Product.objects.filter(owner=request.user)  
    return render(request, 'shop/my_products.html', {'products': products})

@login_required
def reviews(request):
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'shop/reviews.html', {'reviews': reviews})

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('shop:reviews')
    else:
        form = ReviewForm()

    context = {'form': form}    
    return render(request, 'shop/add_review.html', context)