from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
]