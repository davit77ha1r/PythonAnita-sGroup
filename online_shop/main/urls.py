from django.http import HttpResponse
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('index', views.index_page, name="index_page"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('shoplocator', views.shoplocator, name="shoplocator"),
    path('help', views.help, name="help"),
    path('privacy', views.privacy, name="privacy"),
    path('terms', views.terms, name="terms"),
]
