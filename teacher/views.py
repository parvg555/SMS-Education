from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
# Create your views here.

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('index')
    classes = classroom.objects.filter(teacher = request.user)
    context = {
        'classes':classes,
    }
    return render(request,'dashboard.html',context)


def addclass(request):
    if not request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        name = request.POST.get('Class_Name')
        subject = request.POST.get('Subject')
        print(name,subject)
        c = classroom(teacher = request.user, name=name,subject=subject)
        c.save()
        return redirect('dashboard')

    form  = newclass()
    return render(request,'addclass.html',{'form':form})

def Classroom(request,classid):
    return render(request,'classroom.html',{})