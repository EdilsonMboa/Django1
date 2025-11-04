from django.shortcuts import render
from core.models import Product

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