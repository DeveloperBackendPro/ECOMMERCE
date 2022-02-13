from django.urls import path
from order import views
urlpatterns = [
    path('addtoshopcart/<int:pk>/', views.addtoshopcart, name='addtoshopcart'),
    path('shopcart/', views.shopcart, name='shopcart'),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
    path('orderproduct/', views.orderproduct, name='orderproduct'),
]