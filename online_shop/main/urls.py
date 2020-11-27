from django.http import HttpResponse
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('index', views.index_page, name="index_page"),
    path('about', views.about, name="about"),
]
