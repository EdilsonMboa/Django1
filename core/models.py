from django.db import models

class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Price', decimal_places=2, max_digits=10)
    stock = models.IntegerField( 'Available stock')

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField('Name', max_length=100)
    address = models.CharField('Address', max_length=100)
    city = models.CharField('City', max_length=100)
    state = models.CharField('State', max_length=100)
    country = models.CharField('Country', max_length=100)
    area = models.CharField('Area', max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField('Name', max_length=12, blank=True, null=True)
    surname = models.CharField('Surname', max_length=12, blank=True, null=True)
    photo = models.ImageField('Photo', upload_to='clients_photos/', blank=True, null=True)
    country = models.CharField('Country', max_length=20, blank=True, null=True)
    city = models.CharField('City', max_length=20, blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)
    phone = models.CharField('Phone', max_length=12, blank=True, null=True)
    occupation = models.CharField('Occupation', max_length=12, blank=True, null=True)
    birthday = models.DateField('Birthday', blank=True, null=True)
    about = models.TextField('About', blank=True, null=True)
    joined = models.DateField(auto_now_add=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        related_name='employees',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.name} {self.surname}'

