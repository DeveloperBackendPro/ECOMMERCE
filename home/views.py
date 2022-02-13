from django.shortcuts import render,redirect
from django.utils import translation

from home.forms import ContactForm, Comment_detail_Form, NewsLatterForm
from home.models import ContactMessage, FAQ, Blog, Comment_blog, Aboutus, NewsLatter, Slider, Informations
from product.models import Product, Category, Images, Comment
from django.contrib import messages
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)
from django.http import HttpResponseRedirect



def index(request):
    category = Category.objects.filter(status='True').order_by('-id')
    product_latest = Product.objects.filter(status='True').order_by('-id')
    product_slider = Product.objects.filter(status='True').order_by('?')[:6]
    product_picked = Product.objects.filter(status='True').order_by('?')
    slider = Slider.objects.filter(status='True').order_by('-id')
    info = Informations.objects.filter(status='True').order_by('-id')[:1]
    contect = {
        'category':category,
        'product_latest':product_latest,
        'product_slider':product_slider,
        'product_picked':product_picked,
        'slider':slider,
        'info':info,
    }
    return render(request, 'index.html', contect)


def produc_details(request,id, slug):
    category = Category.objects.filter(status='True').order_by('-id')
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    product_latest = Product.objects.filter(status='True').order_by('-id')
    product_slider = Product.objects.filter(status='True').order_by('id')
    product_picked = Product.objects.filter(status='True').order_by('?')
    comments = Comment.objects.filter(product_id=id, status='True')
    info = Informations.objects.filter(status='True').order_by('-id')[:1]
    context = {
        'category':category,
        'product':product,
        'images':images,
        'product_latest': product_latest,
        'product_slider': product_slider,
        'product_picked': product_picked,
        'comments':comments,
        'info':info,
    }
    return render(request, 'product_detail.html', context)



def category_product(request,id, slug):
    category = Category.objects.filter(status='True').order_by('-id')
    categoryies = Category.objects.get(pk=id)
    info = Informations.objects.filter(status='True').order_by('-id')[:1]
    product_latest = Product.objects.filter(status='True').order_by('-id')[:4]
    product_slider = Product.objects.filter(status='True').order_by('id')
    product_picked = Product.objects.filter(status='True').order_by('?')
    product = Product.objects.filter(category_id=id).order_by('-id')
    category_count = product.count()
    paginator = Paginator(product, 9)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
    context = {
        'category': category,
        'product': product,
        'product_latest': product_latest,
        'product_slider': product_slider,
        'product_picked': product_picked,
        'info':info,
        'category_count':category_count,
        'categoryies':categoryies,
    }
    return render(request, 'category_product.html', context)



def contactus(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.phone = form.cleaned_data['phone']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Sizning xabaringiz yuborildi! Rahmat")
            return redirect('index')
    form = ContactForm
    category = Category.objects.filter(status='True').order_by('-id')
    info = Informations.objects.filter(status='True').order_by('-id')[:1]
    context = {'form': form,
               'category':category,
               'info':info,}
    return render(request,'contact-us.html', context)


def faq(request):
    category = Category.objects.filter(status='True').order_by('-id')
    faq = FAQ.objects.filter(status='True').order_by('ordernumber')
    info = Informations.objects.filter(status='True').order_by('-id')[:1]
    context = {
                'category':category,
                'faq': faq,
                'info':info,
              }
    return render(request, 'faqs.html', context)


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        product = Product.objects.filter(title__contains=searched)
        category = Category.objects.filter(status='True').order_by('-id')
        info = Informations.objects.filter(status='True').order_by('-id')[:1]
        context = {
            'category':category,
            'searched':searched,
            'product':product,
            'info':info,
            }
        return render(request, 'search.html', context)


def blog(request):
    category = Category.objects.filter(status='True').order_by('-id')
    info = Informations.objects.filter(status='True').order_by('-id')[:1]
    product_latest = Product.objects.filter(status='True').order_by('?')[:4]
    blog_slider = Blog.objects.filter(status='True').order_by('-id')[:6]
    comment_blog = Comment_blog.objects.all()
    paginator = Paginator(blog_slider, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        blog_slider = paginator.page(page)
    except PageNotAnInteger:
        blog_slider = paginator.page(1)
    except EmptyPage:
        blog_slider = paginator.page(paginator.num_pages)
    context = {
        'category': category,
        'product_latest': product_latest,
        'blog_slider': blog_slider,
        'comment_blog':comment_blog,
        'info':info,
    }
    return render(request,'blog.html', context)


def blog_detail(request,id):
    category = Category.objects.filter(status='True').order_by('-id')
    info = Informations.objects.filter(status='True').order_by('-id')[:1]
    product_latest = Product.objects.filter(status='True').order_by('?')[:4]
    blog_detail = Blog.objects.get(pk=id)
    blog = Blog.objects.filter(status='True').order_by('?')[:4]
    comment_blog = Comment_blog.objects.filter(blog_id=id, status='True')
    context = {
        'category':category,
        'product_latest':product_latest,
        'blog_detail':blog_detail,
        'blog':blog,
        'comment_blog':comment_blog,
        'info':info,
    }
    return render(request, 'blog-detail.html', context)


def comment_blog(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = Comment_detail_Form(request.POST)
        if form.is_valid():
            data = Comment_blog()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.blog_id = id
            data.save()
            messages.success(request, "Sizning izohingiz qabul qilindi !")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)


def about_us(request):
    category = Category.objects.filter(status='True')
    info = Informations.objects.filter(status='True').order_by('-id')[:1]
    aboutus = Aboutus.objects.filter(status='True')[:1]
    context = {
        'category': category,
        'aboutus':aboutus,
        'info':info,
    }
    return render(request, 'about-us.html', context)


def newsLatter(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = NewsLatterForm(request.POST)
        if form.is_valid():
            data = NewsLatter()
            data.email = form.cleaned_data['email']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Sizning emailingiz qabul qilindi!")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)



def selectlanguage(request):
    if request.method == 'POST':
        cur_language = translation.get_language()
        lasturl= request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session['translation.LANGUAGE_SESSION_KEY']=lang
        return redirect("index")