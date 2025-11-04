from django.contrib import admin

from .models import Product, User, Company


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    list_filter = ('name', 'price', 'stock')

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'phone', 'country', 'photo', 'joined', 'company')
    list_filter = ('name', 'surname', 'email', 'phone', 'country', 'photo', 'joined', 'company')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country')
    list_filter = ('name', 'city', 'country')

admin.site.register(Product, ProductAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Company, CompanyAdmin)
