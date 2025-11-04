from django.urls import path

from .views import index, contacto

urlpatterns = [
    path('', index),
    path('contacto', contacto),
]