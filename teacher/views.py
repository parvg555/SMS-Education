from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from recordroom.models import *
from background_task import background
import imaplib
import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
# Create your views here.



@background(schedule = 30)
def mailchecker():
    host = 'imap.gmail.com'
    username = 'smsedu.receive@gmail.com'
    password = 'Sms@edu1234'
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username,password)
    mail.select("inbox")
    _,search_data = mail.search(None,'UNSEEN')
    for num in search_data[0].split():
        _,data = mail.fetch(num , '(RFC822)')
        _,b = data[0]
        email_message = email.message_from_bytes(b)
        for part in email_message.walk():
            if part.get_content_type() == "text/plain" or part.get_content_type() =="text/html":
                body = part.get_payload(decode = True)
                print(body)
                body = str(body)
                body = body.split()
                if body[0] == 'b\'DOUBT':
                    print('DOUBT')
                elif body[0] == 'b\'ANSWER':
                    print('ANSWER')
                else:
                    print('EXCEPTION')


def sendmessage(phone, message, attach = ''):
    print(attach)
    fromaddr = 'smsedu.receive@gmail.com'
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = 'parvg1234@gmail.com'
    msg['Subject'] = str(phone)
    body = message
    msg.attach(MIMEText(body, 'plain'))
    if(attach != ''):
        p = "a"
        attachment = open(os.path.join(settings.MEDIA_ROOT, f'{attach}'),"rb")
        p = MIMEBase('application','octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition',"attachment; filename=%s" % attach)
        msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(fromaddr,'Sms@edu1234')
    text = msg.as_string()
    s.sendmail(fromaddr,'parvg1234@gmail.com',text)
    s.quit()
    return


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
        message = "Hello " + str(name) + ", You have been added to "+str(c.subject)+" classroom with code: "+str(c.id)+".\n in case of doubt type in DOUBT <classroom code> <your message> and send to this number."
        sendmessage(phone,message,"")
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
            sendmessage(i.phone,"SEND",r.title+".wav")
            print(i.phone,r.title) #have to replace with email function
        return redirect('classroom',classid=classid)


    recordings = recording.objects.filter(user = request.user)
    context = {
        'recordings':recordings,
    }
    return render(request,'sendrecording.html',context)


def doubts(request,classid):
    if not request.user.is_authenticated:
        return redirect('index')
    c = classroom.objects.get(pk=classid)
    d = doubt.objects.filter(classroom = c,answered = False)
    context = {
        'doubts':d,
        'classid':classid,
    }
    return render(request,'doubts.html',context)
    pass


def resolve(request, classid, doubtid):
    if not request.user.is_authenticated:
        return request('index')
    c = classroom.objects.get(pk = classid)
    d = doubt.objects.get(pk = doubtid)
    if request.method == 'POST':
        ans = request.POST.get('answer')
        ph = d.student.phone
        d.answered = True
        d.answer = ans
        sendmessage(ph,ans)
        d.save()
        return redirect('doubts',classid = classid)
    context = {
        'doubt':d,
        'classid':classid,
    }
    return render(request,'resolve.html',context)
    pass

def ques(request,classid):
    if not request.user.is_authenticated:
        return redirect('index')
    c = classroom.objects.get(pk = classid)
    ques = question.objects.filter(classroom = c)
    context = {
        'questions':ques,
        'classid':classid,
    }
    return render(request,'questions.html',context)

def askques(request,classid):
    if not request.user.is_authenticated:
        return redirect('index')
    c = classroom.objects.get(pk = classid)
    
    if request.method == 'POST':
        q = request.POST.get('question')
        o1 = request.POST.get('option1')
        o2 = request.POST.get('option2')
        o3 = request.POST.get('option3')
        o4 = request.POST.get('option4')
        correct = request.POST.get('correct')
        ques = question(classroom = c, question = q, option1 = o1, option2 = o2, option3 = o3, option4 = o4, correct = correct)
        ques.save()
        #add send mail function
        return redirect('question',classid = classid)
    
    return render(request,'askques.html',{})

def report(request, classid, questionid):
    if not request.user.is_authenticated:
        return redirect('index')
    
    q = question.objects.get(pk = questionid)
    ans = answer.objects.get(question = q)
    
    pass