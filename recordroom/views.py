from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import *
# Create your views here.

def recordroom(request):
    if not request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        print("reached here")
        audio_file = request.FILES.get('audio_file',None)
        title = request.POST.get('title')
        rec = recording(user = request.user,audio = audio_file,title=title)
        rec.save()
        return render(request,'recorder.html',{})
    

    return render(request,'recorder.html',{})
