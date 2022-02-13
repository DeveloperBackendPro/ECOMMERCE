from django.db import models
from creatoradmin.models import Client
from django.contrib.auth.models import User
from product.models import Product


class ShopCart(models.Model):
    user = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    collar = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0, blank=True, null=True)


    def __str__(self):
        return self.product.title


    @property
    def price(self):
        return (self.product.sell_price)

    @property
    def amount(self):
        return (self.quantity * self.product.sell_price)


class Order(models.Model):
    STATUS = (
        ('Waiting', 'Kuting'),
        ('Accepted', 'Qabul qilingan'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=5, editable=False)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=255)
    address = models.CharField(blank=True, max_length=255)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    feedback = models.CharField(blank=True, max_length=20)
    total = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='Waiting')
    ip = models.CharField(blank=True, max_length=25)
    adminnote = models.CharField(blank=True, max_length=100)
    collar = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    total_quantity = models.IntegerField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

class OrderProduct(models.Model):
    STATUS = (
        ('Waiting', 'Kuting'),
        ('Accepted', 'Qabul qilingan'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2,  blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='Waiting')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title

