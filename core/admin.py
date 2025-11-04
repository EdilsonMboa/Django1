from django.contrib import admin

from .models import Product, Client

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    list_filter = ('name', 'price', 'stock')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email')
    list_filter = ('name', 'surname', 'email')

admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
