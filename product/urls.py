from django.urls import path
from product import views
urlpatterns = [
    path('addcomment/<int:id>', views.addcomment, name='addcomment'),
]