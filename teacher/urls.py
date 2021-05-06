from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/',views.dashboard, name = 'dashboard'),
]