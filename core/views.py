from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from core.models import Product, User

def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contacto.html')

def product(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product' : product
    }
    return render(request, 'product.html', context)

def profile(request, id):
    profile = get_object_or_404(User, id=id)
    context = {
        'profile' : profile
    }
    return render(request, 'profile-page.html', context)