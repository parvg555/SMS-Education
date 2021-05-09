from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('recordroom/',views.recordroom, name = 'recordroom'),
    path('recordings/',views.recordings,name='recordings'),
]