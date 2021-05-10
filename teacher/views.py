from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from recordroom.models import *
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
    if not request.user.is_authenticated:
        return redirect('index')
    
    c = classroom.objects.get(pk = classid)
    students = student.objects.filter(classroom = c)

    
    return render(request,'classroom.html',{
        'classid':classid,
        'students':students,
    })

def addstudent(request,classid):
    if not request.user.is_authenticated:
        return redirect('index')
    
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        c = classroom.objects.get(pk = classid)
        s = student(classroom = c,name = name,phone = phone)
        s.save()
        #have to add welcome message
        return redirect('classroom', classid = classid)
        
    return render(request,'addstudent.html',{})

def sendrecording(request,classid):
    if not request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        recording_id = request.POST.get('audio')
        c = classroom.objects.get(pk = classid)
        r = recording.objects.get(pk = recording_id)
        students = student.objects.filter(classroom = c)
        for i in students:
            print(i.phone,r.title) #have to replace with email function
        return redirect('classroom',classid=classid)


    recordings = recording.objects.filter(user = request.user)
    context = {
        'recordings':recordings,
    }
    return render(request,'sendrecording.html',context)