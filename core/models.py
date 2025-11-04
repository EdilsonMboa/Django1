from django.db import models

class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Price', decimal_places=2, max_digits=10)
    stock = models.IntegerField( 'Available stock')