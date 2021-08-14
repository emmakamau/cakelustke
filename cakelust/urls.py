from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('priceguide/', views.priceguide, name='priceguide'),
    path('flavours/', views.flavours, name='flavours'),
] 