from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from creatoradmin.models import Client
from order.forms import ShopCartForm, OrderForm
from order.models import ShopCart, Order, OrderProduct
from product.models import Product, Category
from django.utils.crypto import get_random_string


@login_required(login_url='login_form')
def addtoshopcart(request, pk):
    url = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=pk)
    user = Client.objects.get(user=request.user)
    data, _ = ShopCart.objects.get_or_create(user=user, product=product)

    if request.method == "POST":
        form = ShopCartForm(request.POST)
        if form.is_valid():
            data.quantity += int(form.cleaned_data.get('quantity'))
            data.collar += form.cleaned_data.get('collar')
            data.size += form.cleaned_data.get('size')
            data.save()
            print('error_1_data')
            messages.success(request, 'Product succeccfully added to shopcart!')
            return redirect(url)
    return redirect(url)


def shopcart(request):
    category = Category.objects.all()
    current_user = request.user
    user = Client.objects.get(user=request.user)
    shopcart = ShopCart.objects.filter(user=user)
    shopcart_all_count = shopcart.count()
    total = 0
    total_qty = 0
    for rs in shopcart:
        total_qty += rs.quantity
        total += rs.product.sell_price * rs.quantity
    context = {
        'shopcart_all_count': shopcart_all_count,
        'user': user,
        'shopcart': shopcart,
        'category': category,
        'total': total,
        'total_qty': total_qty,
        'current_user': current_user,
    }
    return render(request, 'shopcart.html', context)


@login_required(login_url='login_form')
def deletefromcart(request, id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, "Your item deleted from Shop Cart!")
    return redirect('shopcart')


def orderproduct(request):
    client = Client.objects.get(user=request.user)
    shopcart_ = ShopCart.objects.filter(user=client)
    current_user = request.user
    total_quantity = 0
    total = 0
    size = 0
    collar = 0


    for rs in shopcart_:
        total += rs.product.sell_price * rs.quantity
        total_quantity += rs.quantity
        size = rs.size
        collar = rs.collar





    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data.get('first_name', None)
            data.last_name = form.cleaned_data.get('last_name', None)
            data.address = form.cleaned_data.get('address', None)
            data.phone = form.cleaned_data.get('phone', None)
            data.country = form.cleaned_data.get('country', None)
            data.city = form.cleaned_data.get('city', None)
            data.email = form.cleaned_data.get('email', None)
            data.feedback = form.cleaned_data.get('feedback', None)




            data.collar = collar
            data.size = size


            data.user_id = request.user.id
            data.total = total
            data.total_quantity = total_quantity
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(10).upper()  # random code
            data.code = ordercode
            data.save()

            client = Client.objects.get(user=request.user)
            shopcart_ = ShopCart.objects.filter(user=client)
            for rs in shopcart_:
                detail = OrderProduct()
                detail.order_id = data.id  # Order id
                detail.product_id = rs.product_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity
                detail.price = rs.product.sell_price
                detail.size = rs.size
                detail.collar = rs.collar
                detail.save()
                product = Product.objects.get(id=rs.product_id)
                product.save()

            ShopCart.objects.filter(user=client).delete()
            request.session['cart_items'] = 0
            messages.success(request, "Your Order Has Been Completed! Thank you!")
            return redirect('index')
        else:
            messages.warning(request, form.errors)
            return redirect('orderproduct')

    form = OrderForm
    client = Client.objects.get(user=request.user)
    shopcart_ = ShopCart.objects.filter(user_id=client)
    context = {
        'shopcart': shopcart_,
        'total': total,
        'client': client,
        'form': form,
    }

    return render(request, 'checkout.html', context)
