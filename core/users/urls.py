from django.contrib import admin
from django.urls import path
 

from .views import login_view, register_view, login_view_django

urlpatterns = [
    path('login/', login_view_django, name='login'), 
    path('register/', register_view, name='register'),
]
