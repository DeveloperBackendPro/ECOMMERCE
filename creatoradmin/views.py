from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from creatoradmin.forms import SignUpForm, AddCategoryForm, UserUpdateForm, ProfileUpdateForm, AddInformationsForm, \
    EditInformationsForm, EditCategoryForm, AddProductsForm, EditProductsForm, EditOrderProductForm, AppandDetailsForm, \
    EditDetailsForm, AppandBlogForm, EditBlogForm, AppandAboutForm, EditAboutForm, AppandFAQSForm, EditFAQSForm, \
    EditContactForm, EditComentsBlogForm, EditCommentProductForm, UserPermissonForm, AppandSliderForm, EditSliderForm, \
    UserClientUpdateForm, ProfileClinetUpdateForms
from creatoradmin.models import Client, Creator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from home.models import ContactMessage, Informations, Blog, Aboutus, FAQ, NewsLatter, Comment_blog, Slider
from order.models import Order, OrderProduct, ShopCart
from product.models import Category, Product, Images, Comment
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)
from django.utils import translation
from django.http import HttpResponseRedirect


########################################################################################################################
######################################## CREATOR QISMI #################################################################
########################################################################################################################


@login_required(login_url='login_form')
def register_creator(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            data = Creator()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            messages.success(request, 'Your account has been created!')
            return redirect('user_update')
        else:
            messages.warning(request, form.errors)
            return redirect('register_creator')
    form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'Authenticate/register_creator.html', context)


def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                Creator.objects.get(user_id=request.user.id)
                return redirect('creator')
            except:
                try:
                    Client.objects.get(user_id=request.user.id)
                    return redirect('client')
                except:
                    return redirect('login_form')
        else:
            messages.warning(request, "Login Error! User name or Password is incorrect")
            return redirect('login_form')
    return render(request, 'Authenticate/login.html')


@login_required(login_url='login_form')
def creator(request):
    try:
        creator = Creator.objects.get(user=request.user)
    except:
        messages.warning(request, 'Error Try Again Later')
        return redirect('login_form')
    category = Category.objects.filter(status='True')
    product = Product.objects.filter(status='True')
    client = Client.objects.all()
    contact = ContactMessage.objects.all()
    order = Order.objects.all()
    order_product = OrderProduct.objects.all()
    order_product_count = order_product.count()
    category_count = category.count()
    product_count = product.count()
    client_count = client.count()
    contact_count = contact.count()
    context = {
        'client':client,
        'creator':creator,
        'category':category,
        'product':product,
        'contact':contact,
        'order':order,
        'order_product':order_product,
        'category_count':category_count,
        'product_count':product_count,
        'client_count':client_count,
        'contact_count':contact_count,
        'order_product_count':order_product_count,
    }
    return render(request, 'Creator/creator.html', context)





@login_required(login_url='login_form')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance = request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.creator)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('creator')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.creator)
        creator = Creator.objects.get(user=request.user)
        context = {
             'user_form': user_form,
             'profile_form': profile_form,
             'creator':creator,
             }
        return render(request, 'Authenticate/user_update.html', context)


def logout_form(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login_form')
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your profile password successfully updated')
            return redirect('creator')
        else:
            messages.error(request, 'Eror password')
            return redirect('user_password')
    else:
        form = PasswordChangeForm(request.user)
        creator = Creator.objects.get(user=request.user)
        context = {
            'form':form,
            'creator':creator,
        }
        return render(request, 'Authenticate/user_password.html',context)
########################################################################################################################
######################################## CLIENT QISMI ##################################################################
########################################################################################################################

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            data = Client()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            messages.success(request, 'Your account has been created!')
            return redirect('user_update_client')
        else:
            messages.warning(request, form.errors)
            return redirect('register')
    form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'Authenticate/register.html', context)





@login_required(login_url='login_form')
def client(request):
    try:
        client = Client.objects.get(user=request.user)
    except:
        messages.warning(request, 'Error Try Again Later')
        return redirect('login_form')
    current_user = request.user
    order_product = OrderProduct.objects.filter(user_id=current_user.id)
    order_product_count = order_product.count()
    context = {
        'client':client,
        'order_product':order_product,
        'order_product_count':order_product_count,
    }
    return render(request, 'Clients/client.html', context)



@login_required(login_url='login_form')
def user_update_client(request):
    if request.method == 'POST':
        user_form = UserClientUpdateForm(request.POST, instance = request.user)
        profile_form = ProfileClinetUpdateForms(request.POST, request.FILES, instance = request.user.client)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('client')
    else:
        user_form = UserClientUpdateForm(instance=request.user)
        profile_form = ProfileClinetUpdateForms(instance=request.user.client)
        client = Client.objects.get(user=request.user)
        context = {
             'user_form': user_form,
             'profile_form': profile_form,
             'client':client,
             }
        return render(request, 'Clients/user_update_client.html', context)



@login_required(login_url='login_form')
def user_password_client(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your profile password successfully updated')
            return redirect('client')
        else:
            messages.error(request, 'Eror password')
            return redirect('user_password_client')
    else:
        form = PasswordChangeForm(request.user)
        client = Client.objects.get(user=request.user)
        context = {
            'form':form,
            'client':client,
        }
        return render(request, 'Clients/user_password_client.html',context)



@login_required(login_url='login_form')
def user_orders_product(request):
    current_user = request.user
    order_product = OrderProduct.objects.filter(user_id=current_user.id)
    client = Client.objects.get(user=request.user)
    context = {
                'order_product': order_product,
                'client':client,
    }
    return render(request, 'Clients/user_order_product_client.html', context)

@login_required(login_url='login_form')
def user_order_product_detail_client(request,id, oid):
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=oid)
    orderitem = OrderProduct.objects.filter(id=id,user_id=current_user.id)
    client = Client.objects.get(user=request.user)
    context = {
                'orderitem': orderitem,
                'client':client,
                'order':order,
    }
    return render(request, 'Clients/user_order_product_detail_client.html', context)

@login_required(login_url='login_form')
def order_delate_client(request, pk):
    current_user = request.user
    orderproduct = OrderProduct.objects.filter(id=pk,user_id=current_user.id)
    order = Order.objects.get(id=pk,user_id=current_user.id)
    orderproduct.delete()
    order.delete()
    return redirect('user_orders_product')

########################################################################################################################
######################################## INFORMATSION ##################################################################
########################################################################################################################

def addinformatsions(request):
    if request.method == 'POST':
        form = AddInformationsForm(request.POST, request.FILES)
        if form.is_valid():
            info = Informations()
            info.title_uz = form.cleaned_data.get('title_uz')
            info.title_en = form.cleaned_data.get('title_en')
            info.title_ru = form.cleaned_data.get('title_ru')
            info.country = form.cleaned_data.get('country')
            info.city = form.cleaned_data.get('city')
            info.address_en = form.cleaned_data.get('address_en')
            info.address_ru = form.cleaned_data.get('address_ru')
            info.address_uz = form.cleaned_data.get('address_uz')
            info.phone = form.cleaned_data.get('phone')
            info.email = form.cleaned_data.get('email')
            info.telegram = form.cleaned_data.get('telegram')
            info.instagram = form.cleaned_data.get('instagram')
            info.facebook = form.cleaned_data.get('facebook')
            info.twitter = form.cleaned_data.get('twitter')
            if request.FILES:
                info.image = request.FILES['image']
            info.location = form.cleaned_data.get('location')
            info.description_uz = form.cleaned_data.get('description_uz')
            info.description_en = form.cleaned_data.get('description_en')
            info.description_ru = form.cleaned_data.get('description_ru')
            info.status = form.cleaned_data.get('status')
            info.save()
            messages.success(request, 'Your account has been updated')
            return redirect('informatsion_update')
        else:
            messages.error(request, 'Eror password')
            return redirect('addinformatsions')

    form = AddInformationsForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Informations/add_informatsion.html', context)


def informatsion_update(request):
    info = Informations.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(info, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        info = paginator.page(page)
    except PageNotAnInteger:
        info = paginator.page(1)
    except EmptyPage:
        info = paginator.page(paginator.num_pages)
    context = {
        'info': info,
        'creator': creator,
    }
    return render(request, 'Informations/info_update.html', context)


def info_edit(request, id):
    info = Informations.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditInformationsForm(request.POST, request.FILES, instance=info)
        if request.FILES:
            info.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('informatsion_update')
        else:
            messages.error(request, 'Eror password')
            return redirect("info_edit")
    else:
        form = EditInformationsForm(instance=info)
        context = {'form': form,
                'creator': creator,
                'info':info,}

        return render(request, 'Informations/info_edit.html', context)


def info_delate(request, id):
    info = Informations.objects.get(pk=id)
    info.delete()
    return redirect('informatsion_update')


def info_delate_all(request):
    info = Informations.objects.all()
    info.delete()
    return redirect('informatsion_update')
########################################################################################################################
########################################## CATEGORY ####################################################################
########################################################################################################################


def addcategory(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = Category()
            category.title_uz = form.cleaned_data.get('title_uz')
            category.title_en = form.cleaned_data.get('title_en')
            category.title_ru = form.cleaned_data.get('title_ru')
            category.description_uz = form.cleaned_data.get('description_uz')
            category.description_en = form.cleaned_data.get('description_en')
            category.description_ru = form.cleaned_data.get('description_ru')
            if request.FILES:
                category.image = request.FILES['image']
            category.slug = form.cleaned_data.get('slug')
            category.status = form.cleaned_data.get('status')
            category.save()
            return redirect('category_update')
    form = AddCategoryForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Category/add-category.html', context)


def category_update(request):
    category = Category.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(category, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        category = paginator.page(page)
    except PageNotAnInteger:
        category = paginator.page(1)
    except EmptyPage:
        category = paginator.page(paginator.num_pages)
    context = {
        'category': category,
        'creator': creator,
    }
    return render(request, 'Category/category_update.html', context)


def category_edit(request, id):
    category = Category.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditCategoryForm(request.POST, request.FILES, instance=category)
        if request.FILES:
            category.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('category_update')
        else:
            messages.error(request, 'Eror password')
            return redirect('category_edit')
    else:
        form = EditCategoryForm(instance=category)
        context = {'form': form,
                'creator': creator,
                'category':category,}

        return render(request, 'Category/category_edit.html', context)


def category_delate(request, id):
    category = Category.objects.get(pk=id)
    category.delete()
    return redirect('category_update')


def category_delate_all(request):
    category = Category.objects.all()
    category.delete()
    return redirect('category_update')


########################################################################################################################
########################################## PRODUCTS ####################################################################
########################################################################################################################

def addproduct(request):
    if request.method == 'POST':
        form = AddProductsForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product()
            product.category = form.cleaned_data.get('category')
            product.title_uz = form.cleaned_data.get('title_uz')
            product.title_en = form.cleaned_data.get('title_en')
            product.title_ru = form.cleaned_data.get('title_ru')
            product.old_price = form.cleaned_data.get('old_price')
            product.sell_price = form.cleaned_data.get('sell_price')
            if request.FILES:
                product.image = request.FILES['image']
            product.slug = form.cleaned_data.get('slug')
            product.status = form.cleaned_data.get('status')
            product.description_uz = form.cleaned_data.get('description_uz')
            product.description_en = form.cleaned_data.get('description_en')
            product.description_ru = form.cleaned_data.get('description_ru')
            product.save()
            return redirect('product_update')
    form = AddProductsForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Product/add_product.html', context)


def product_update(request):
    product = Product.objects.filter(status='True').order_by('-id')
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(product, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
    context = {
        'product': product,
        'creator': creator,
    }
    return render(request, 'Product/product_update.html', context)


def product_edit(request, id):
    product = Product.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditProductsForm(request.POST, request.FILES, instance=product)
        if request.FILES:
            product.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('product_update')
        else:
            messages.error(request, 'Eror password')
            return redirect('product_edit')
    else:
        form = EditProductsForm(instance=product)
        context = {'form': form,
                'creator': creator,
                'product':product,}

        return render(request, 'Product/product_edit.html', context)


def product_delate(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('product_update')


def product_delate_all(request):
    product = Product.objects.all()
    product.delete()
    return redirect('product_update')

########################################################################################################################
########################################## ORDERSSS ####################################################################
########################################################################################################################
def order_all(request):
    orderall = OrderProduct.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(orderall, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        orderall = paginator.page(page)
    except PageNotAnInteger:
        orderall = paginator.page(1)
    except EmptyPage:
        orderall = paginator.page(paginator.num_pages)
    context = {
        'orderall': orderall,
        'creator': creator,
    }
    return render(request, 'Orders/orders_page.html', context)


def orders(request,id):
    orderproduct = OrderProduct.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditOrderProductForm(request.POST, instance=orderproduct)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('order_all')
        else:
            messages.error(request, 'Eror password')
            return redirect('orders')
    else:
        form = EditOrderProductForm(instance=orderproduct)

    context = {
        'form':form,
        'orderproduct': orderproduct,
        'creator': creator,
    }
    return render(request, 'Orders/order_detail.html', context)


def order_delate(request, pk):
    orderprpduct = OrderProduct.objects.get(id=pk)
    order = Order.objects.get(id=pk)
    orderprpduct.delete()
    order.delete()
    return redirect('order_all')


def order_delate_all(request):
    orderprpduct = OrderProduct.objects.all()
    order = Order.objects.all()
    orderprpduct.delete()
    order.delete()
    return redirect('order_all')


########################################################################################################################
########################################## PRODUCT DETAILS #############################################################
########################################################################################################################

def apanddetail(request):
    if request.method == 'POST':
        form = AppandDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            details = Images()
            details.product = form.cleaned_data.get('product')
            if request.FILES:
                details.image = request.FILES['image']
            details.collor = form.cleaned_data.get('collor')
            details.size = form.cleaned_data.get('size')
            details.save()
            return redirect('details_update')
    form = AppandDetailsForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Details/add_details.html', context)


def details_update(request):
    detail = Images.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(detail, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        detail = paginator.page(page)
    except PageNotAnInteger:
        detail = paginator.page(1)
    except EmptyPage:
        detail = paginator.page(paginator.num_pages)
    context = {
        'detail': detail,
        'creator': creator,
    }
    return render(request, 'Details/details_update.html', context)


def detail_edit(request, id):
    detail = Images.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditDetailsForm(request.POST, request.FILES, instance=detail)
        if request.FILES:
            detail.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('details_update')
        else:
            messages.error(request, 'Eror password')
            return redirect('detail_edit')
    else:
        form = EditDetailsForm(instance=detail)
        context = {'form': form,
                'creator': creator,
                'detail':detail,}

        return render(request, 'Details/detail_edit.html', context)



def detail_delate(request, id):
    detail = Images.objects.get(pk=id)
    detail.delete()
    return redirect('details_update')


def detail_delate_all(request):
    detail = Images.objects.all()
    detail.delete()
    return redirect('details_update')

########################################################################################################################
########################################## BLOG ########################################################################
########################################################################################################################
def apandblog(request):
    if request.method == 'POST':
        form = AppandBlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = Blog()
            blog.title_uz = form.cleaned_data.get('title_uz')
            blog.title_en = form.cleaned_data.get('title_en')
            blog.title_ru = form.cleaned_data.get('title_ru')
            if request.FILES:
                blog.image = request.FILES['image']
            blog.status = form.cleaned_data.get('status')
            blog.description_uz = form.cleaned_data.get('description_uz')
            blog.description_en = form.cleaned_data.get('description_en')
            blog.description_ru = form.cleaned_data.get('description_ru')
            blog.save()
            return redirect('blog_update')
    form = AppandBlogForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Blog/add_blog.html', context)


def blog_update(request):
    blog = Blog.objects.filter(status='True')
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(blog, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage:
        blog = paginator.page(paginator.num_pages)
    context = {
        'blog': blog,
        'creator': creator,
    }
    return render(request, 'Blog/blog_update.html', context)


def blog_edit(request, id):
    blog = Blog.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditBlogForm(request.POST, request.FILES, instance=blog)
        if request.FILES:
            blog.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('blog_update')
        else:
            messages.error(request, 'Eror password')
            return redirect('blog_edit')
    else:
        form = EditBlogForm(instance=blog)
        context = {'form': form,
                'creator': creator,
                'blog':blog,}

        return render(request, 'Blog/blog_edit.html', context)


def blog_delate(request, id):
    blog = Blog.objects.get(pk=id)
    blog.delete()
    return redirect('blog_update')


def blog_delate_all(request):
    blog = Blog.objects.all()
    blog.delete()
    return redirect('blog_update')

########################################################################################################################
########################################## ABOUT US ####################################################################
########################################################################################################################
def apandabout(request):
    if request.method == 'POST':
        form = AppandAboutForm(request.POST, request.FILES)
        if form.is_valid():
            about = Aboutus()
            about.title_uz = form.cleaned_data.get('title_uz')
            about.title_en = form.cleaned_data.get('title_en')
            about.title_ru = form.cleaned_data.get('title_ru')
            if request.FILES:
                about.image = request.FILES['image']
            about.status = form.cleaned_data.get('status')
            about.description_uz = form.cleaned_data.get('description_uz')
            about.description_en = form.cleaned_data.get('description_en')
            about.description_ru = form.cleaned_data.get('description_ru')
            about.save()
            return redirect('about_update')
    form = AppandAboutForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Aboutus/add_about.html', context)


def about_update(request):
    about = Aboutus.objects.filter(status='True')
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(about, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        about = paginator.page(page)
    except PageNotAnInteger:
        about = paginator.page(1)
    except EmptyPage:
        about = paginator.page(paginator.num_pages)
    context = {
        'about': about,
        'creator': creator,
    }
    return render(request, 'Aboutus/about_update.html', context)


def about_edit(request, id):
    about = Aboutus.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditAboutForm(request.POST, request.FILES, instance=about)
        if request.FILES:
            about.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('about_update')
        else:
            messages.error(request, 'Eror password')
            return redirect('about_edit')
    else:
        form = EditAboutForm(instance=about)
        context = {'form': form,
                'creator': creator,
                'about':about,}

        return render(request, 'Aboutus/about_edit.html', context)


def about_delate(request, id):
    about = Aboutus.objects.get(pk=id)
    about.delete()
    return redirect('about_update')


def about_delate_all(request):
    about = Aboutus.objects.all()
    about.delete()
    return redirect('about_update')

########################################################################################################################
########################################## FAQ  ########################################################################
########################################################################################################################
def apandfaqs(request):
    if request.method == 'POST':
        form = AppandFAQSForm(request.POST)
        if form.is_valid():
            faq = FAQ()
            faq.ordernumber = form.cleaned_data.get('ordernumber')
            faq.question_en = form.cleaned_data.get('question_en')
            faq.question_ru = form.cleaned_data.get('question_ru')
            faq.question_uz = form.cleaned_data.get('question_uz')
            faq.status = form.cleaned_data.get('status')
            faq.answer_uz = form.cleaned_data.get('answer_uz')
            faq.answer_en = form.cleaned_data.get('answer_en')
            faq.answer_ru = form.cleaned_data.get('answer_ru')
            faq.save()
            return redirect('faq_update')
    form = AppandFAQSForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Faq/add_faq.html', context)



def faq_update(request):
    faq = FAQ.objects.filter(status='True').order_by('-id')
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(faq, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        faq = paginator.page(page)
    except PageNotAnInteger:
        faq = paginator.page(1)
    except EmptyPage:
        faq = paginator.page(paginator.num_pages)
    context = {
        'faq': faq,
        'creator': creator,
    }
    return render(request, 'Faq/faq_update.html', context)


def faq_edit(request, id):
    faq = FAQ.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditFAQSForm(request.POST, request.FILES, instance=faq)
        if request.FILES:
            faq.image = request.FILES['image']
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('faq_update')
        else:
            messages.error(request, 'Eror password')
            return redirect('faq_edit')
    else:
        form = EditFAQSForm(instance=faq)
        context = {'form': form,
                'creator': creator,
                'faq':faq,}

        return render(request, 'Faq/faq_edit.html', context)



def faq_delate(request, id):
    faq = FAQ.objects.get(pk=id)
    faq.delete()
    return redirect('faq_update')


def faq_delate_all(request):
    faq = FAQ.objects.all()
    faq.delete()
    return redirect('faq_update')


########################################################################################################################
########################################## NEWSLATTER  #################################################################
########################################################################################################################
def newslatter_get(request):
    newslatter = NewsLatter.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(newslatter, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        newslatter = paginator.page(page)
    except PageNotAnInteger:
        newslatter = paginator.page(1)
    except EmptyPage:
        newslatter = paginator.page(paginator.num_pages)
    context = {
        'newslatter': newslatter,
        'creator': creator,
    }
    return render(request, 'Newslatter/newslatter_get.html', context)

def newslatter_delate(request, id):
    newslatter = NewsLatter.objects.get(pk=id)
    newslatter.delete()
    return redirect('newslatter_get')


def newslatter_delate_all(request):
    newslatter = NewsLatter.objects.all()
    newslatter.delete()
    return redirect('newslatter_get')


########################################################################################################################
########################################## CONTACTUS  ##################################################################
########################################################################################################################
def contact_get(request):
    contact = ContactMessage.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(contact, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        contact = paginator.page(page)
    except PageNotAnInteger:
        contact = paginator.page(1)
    except EmptyPage:
        contact = paginator.page(paginator.num_pages)
    context = {
        'contact': contact,
        'creator': creator,
    }
    return render(request, 'Contact/contact_get.html', context)



def contact_edit(request, id):
    contact = ContactMessage.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('contact_get')
        else:
            messages.error(request, 'Eror password')
            return redirect('contact_edit')
    else:
        form = EditContactForm(instance=contact)
        context = {'form': form,
                'creator': creator,
                'contact':contact,}

        return render(request, 'Contact/contact_edit.html', context)


def contact_delate(request, id):
    contact = ContactMessage.objects.get(pk=id)
    contact.delete()
    return redirect('contact_get')


def contact_delate_all(request):
    contact = ContactMessage.objects.all()
    contact.delete()
    return redirect('contact_get')

########################################################################################################################
########################################## BLOG COMMENTS  ##############################################################
########################################################################################################################
def comment_blog_get(request):
    comment = Comment_blog.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(comment, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        comment = paginator.page(page)
    except PageNotAnInteger:
        comment = paginator.page(1)
    except EmptyPage:
        comment = paginator.page(paginator.num_pages)
    context = {
        'comment': comment,
        'creator': creator,
    }
    return render(request, 'Blog_Comment/comment_blog_get.html', context)


def comment_blog_edit(request, id):
    comment = Comment_blog.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditComentsBlogForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('comment_blog_get')
        else:
            messages.error(request, 'Eror password')
            return redirect('comment_edit')
    else:
        form = EditComentsBlogForm(instance=comment)
        context = {'form': form,
                'creator': creator,
                'comment':comment,}

        return render(request, 'Blog_Comment/comment_blog_edit.html', context)


def coment_blog_delate(request, id):
    coment_blog = Comment_blog.objects.get(pk=id)
    coment_blog.delete()
    return redirect('comment_blog_get')


def coment_blog_delate_all(request):
    coment_blog = Comment_blog.objects.all()
    coment_blog.delete()
    return redirect('comment_blog_get')


########################################################################################################################
########################################## PRODUCTS COMMENTS  ##########################################################
########################################################################################################################

def comment_product_get(request):
    product_comment = Comment.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(product_comment, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        product_comment = paginator.page(page)
    except PageNotAnInteger:
        product_comment = paginator.page(1)
    except EmptyPage:
        product_comment = paginator.page(paginator.num_pages)
    context = {
        'product_comment': product_comment,
        'creator': creator,
    }
    return render(request, 'Product_Comment/comment_product_get.html', context)


def comment_product_edit(request, id):
    product_edit = Comment.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditCommentProductForm(request.POST, instance=product_edit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('comment_product_get')
        else:
            messages.error(request, 'Eror password')
            return redirect('comment_product_edit')
    else:
        form = EditCommentProductForm(instance=product_edit)
        context = {'form': form,
                'creator': creator,
                'product_edit':product_edit,}

        return render(request, 'Product_Comment/comment_product_edit.html', context)


def coment_product_delate(request, id):
    coment_product = Comment.objects.get(pk=id)
    coment_product.delete()
    return redirect('comment_product_get')


def coment_product_delate_all(request):
    coment_product = Comment.objects.all()
    coment_product.delete()
    return redirect('comment_product_get')

########################################################################################################################
########################################## USER PERMISSION  ############################################################
########################################################################################################################
def apanduserpermission(request,id):
    if request.method == 'POST':
        form = UserPermissonForm(request.POST, request.FILES)
        if form.is_valid():
            creator = Creator()
            creator.user = form.cleaned_data.get('user')
            # creator.phone = form.cleaned_data.get('phone')
            # creator.address = form.cleaned_data.get('address')
            # creator.city = form.cleaned_data.get('city')
            if request.FILES:
                creator.image = request.FILES['image']
            # creator.country = form.cleaned_data.get('country')
            client = Client.objects.get(pk=id)
            client.delete()
            creator.save()
            return redirect('creator')
    form = UserPermissonForm()
    client = Client.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
        'client':client,
    }
    return render(request, 'Add_Creator/add_user_permission.html', context)

def users_get(request):
    users = Client.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(users, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
        'users': users,
        'creator': creator,
    }
    return render(request, 'Add_Creator/get_users.html', context)

def users_delete(request, id):
    client = Client.objects.get(pk=id)
    client.delete()
    return redirect('users_get')

def users_delete_delate_all(request):
    client = Client.objects.all()
    client.delete()
    return redirect('users_get')

########################################################################################################################
########################################## PRODUCT GALLERY  ############################################################
########################################################################################################################
def product_gallery(request):
    product = Product.objects.all()
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(product, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
    context = {
        'product': product,
        'creator': creator,
    }
    return render(request, 'Product_gallery/gallery.html', context)


def product_gallery_id(request, id):
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    creator = Creator.objects.get(user=request.user)
    context = {
        'product': product,
        'creator': creator,
        'images':images,
    }
    return render(request, 'Product_gallery/gallery_id.html', context)

########################################################################################################################
################################################   SLIDER   ############################################################
########################################################################################################################
def apandslider(request):
    if request.method == 'POST':
        form = AppandSliderForm(request.POST, request.FILES)
        if form.is_valid():
            slider = Slider()
            slider.title_en = form.cleaned_data.get('title_en')
            slider.title_ru = form.cleaned_data.get('title_ru')
            slider.title_uz = form.cleaned_data.get('title_uz')
            if request.FILES:
                slider.image = request.FILES['image']
            slider.description_uz = form.cleaned_data.get('description_uz')
            slider.description_en = form.cleaned_data.get('description_en')
            slider.description_ru = form.cleaned_data.get('description_ru')
            slider.save()
            return redirect('slider_update')
    form = AppandSliderForm()
    creator = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'creator': creator,
    }
    return render(request, 'Slider/add_slider.html', context)



def slider_update(request):
    slider = Slider.objects.filter(status='True').order_by('-id')
    creator = Creator.objects.get(user=request.user)
    paginator = Paginator(slider, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        slider = paginator.page(page)
    except PageNotAnInteger:
        slider = paginator.page(1)
    except EmptyPage:
        slider = paginator.page(paginator.num_pages)
    context = {
        'slider': slider,
        'creator': creator,
    }
    return render(request, 'Slider/update_slider.html', context)

def slider_edit(request, id):
    slider = Slider.objects.get(pk=id)
    creator = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditSliderForm(request.POST, instance=slider)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('slider_update')
        else:
            messages.error(request, 'Eror password')
            return redirect('slider_edit')
    else:
        form = EditSliderForm(instance=slider)
        context = {'form': form,
                'creator': creator,
                'slider':slider,}

        return render(request, 'Slider/edit_slider.html', context)


def slider_delate(request, id):
    slider = Slider.objects.get(pk=id)
    slider.delete()
    return redirect('slider_update')


def slider_delate_all(request):
    slider = Slider.objects.all()
    slider.delete()
    return redirect('slider_update')

########################################################################################################################
########################################################################################################################
########################################################################################################################



def searched(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        product = Product.objects.filter(title__contains=searched)
        category = Category.objects.filter(status='True').order_by('-id')
        creator = Creator.objects.get(user=request.user)
        context = {
            'category':category,
            'searched':searched,
            'product':product,
            'creator':creator,
            }
        return render(request, 'Searched/searched.html', context)


def selectlanguage_admin(request):
    if request.method == 'POST':
        cur_language = translation.get_language()
        lasturl= request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session['translation.LANGUAGE_SESSION_KEY']=lang
        return redirect("creator")



def selectlanguage_client(request):
    if request.method == 'POST':
        cur_language = translation.get_language()
        lasturl= request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session['translation.LANGUAGE_SESSION_KEY']=lang
        return redirect("client")