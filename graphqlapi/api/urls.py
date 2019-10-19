from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('ingredient/', views.ingredient, name='ingredient'),
    path('detail/', views.detail, name='detail'),
    
]