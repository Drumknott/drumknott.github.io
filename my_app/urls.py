from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('products.html', views.products),
    path('aboutMe.html', views.about_me)
]
