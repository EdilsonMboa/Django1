import profile
from itertools import product

from django.urls import path

from .views import index, contact, product, profile

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('product/<int:id>', product, name='product'),
    path('profile/<int:id>', profile, name='profile'),
]