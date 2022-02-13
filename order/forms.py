from django import forms
from order.models import ShopCart, Order


class ShopCartForm(forms.ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity', 'collar', 'size',]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'phone', 'email', 'city', 'country','feedback',]