from django.urls import path
from home import views
urlpatterns = [
    path('', views.index, name='index'),
    path('faq/', views.faq, name='faq'),
    path('search/', views.search, name='search'),
    path('blog/', views.blog, name='blog'),
    path('blog_detail//<int:id>', views.blog_detail, name='blog_detail'),
    path('comment_blog/<int:id>', views.comment_blog, name='comment_blog'),
    path('contactus/', views.contactus, name='contactus'),
    path('newsLatter/', views.newsLatter, name='newsLatter'),
    path('about_us/', views.about_us, name='about_us'),
    path('produc_details/<int:id>/<slug:slug>', views.produc_details, name='produc_details'),
    path('category/<int:id>/<slug:slug>',views.category_product, name='category_product'),
]