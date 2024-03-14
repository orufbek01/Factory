from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator





class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="maxsulot turi")

    def __str__(self):
        return self.name


class User(models.Model):
    phone_number = models.CharField(max_length=13, verbose_name="telefon raqam", unique=True, null=True, blank=True, validators=[
        RegexValidator(
            regex=r'^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='Invalid number'
        )
    ])
    extra_phone_number = models.CharField(max_length=13,verbose_name="qo'shimcha telefon raqam", unique=True, null=True, blank=True, validators=[
        RegexValidator(
            regex=r'^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='Invalid number'
        )
    ])
    address = models.TextField()

    def __str__(self):
        return self.phone_number

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Image(models.Model):
    image = models.ImageField(upload_to='product_images/', verbose_name="maxsulot rasmi", )

    def __str__(self):
        return self.image


class Product(models.Model):
    name = models.CharField(max_length=100 ,verbose_name="nomi",)
    category = models.ForeignKey(Category,verbose_name="maxsulot turi tanlash", on_delete=models.CASCADE)
    description = models.CharField(max_length=255, verbose_name="tarif",)
    price = models.DecimalField(max_digits=10, verbose_name="narxi", decimal_places=2)
    quantity = models.IntegerField(verbose_name="miqdori",)
    photo = models.ManyToManyField('Image', verbose_name="rasm tanlash", related_name='products')
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User,verbose_name="mijoz tanlash", on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,verbose_name="maxsulot tanlash", through='OrderProduct')
    quantity = models.IntegerField(verbose_name="miqdori",)
    PAYMENT_CHOICES = (
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('click', 'Click'),
    )
    payment = models.CharField(max_length=10,verbose_name="to'lov turi", choices=PAYMENT_CHOICES)
    total_price = models.DecimalField(max_digits=10,verbose_name="jami narxi", decimal_places=2)

    def __str__(self):
        return self.user
