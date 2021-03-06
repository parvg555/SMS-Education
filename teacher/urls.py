from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/',views.dashboard, name = 'dashboard'),
    path('addclass/',views.addclass,name='addclass'),
    path('classroom/<int:classid>/',views.Classroom, name='classroom'),
    path('classroom/<int:classid>/addstudent/',views.addstudent, name='addstudent'),
    path('classroom/<int:classid>/sendrecording/',views.sendrecording, name='sendrecording'),
    path('classroom/<int:classid>/question/',views.ques, name='question'),
    path('classroom/<int:classid>/askques/',views.askques,name='askques'),
    path('classroom/<int:classid>/doubts',views.doubts,name='doubts'),
    path('classroom/<int:classid>/resolve/<int:doubtid>/',views.resolve,name='resolve'),
    path('classroom/<int:classid>/report/<int:questionid>/',views.report,name='report'),
]

