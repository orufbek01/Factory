from django.shortcuts import render
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class Region(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields related to Region if needed

    def  __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields related to Category if needed
    def __str__(self):
        return self.name



class User(models.Model):
    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True, validators=[
        RegexValidator(
            regex=r'^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='Invalid number'
        )
    ])
    extra_phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True, validators=[
        RegexValidator(
            regex=r'^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='Invalid number'
        )
    ])
    region = models.ForeignKey(Region, on_delete=models.CASCADE,)
    address = models.TextField()
    # Add other fields related to User if needed

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    photo = models.ManyToManyField('Image', related_name='products')
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    # Add other fields related to Product if needed

class Image(models.Model):
    image = models.ImageField(upload_to='product_images/')

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    quantity = models.IntegerField()
    PAYMENT_CHOICES = (
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('click', 'Click'),
    )
    payment = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)




