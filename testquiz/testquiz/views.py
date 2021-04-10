from django.shortcuts import render
from testquiz.models import Exam
from testquiz.models import Newuser

from django.contrib import messages

def indexpage(request):
    return render(request,'index.html')

def examonline(request):
    results=Exam.objects.all()
    return render(request,'quiz.html',{"Exam":results})
    

def register(request):
    if request.method=='POST':
        Username=request.POST['Username']
        Email=request.POST['Email']
        Passwrd=request.POST['Password']
        Newuser(Username=Username,Email=Email,Passwrd=Passwrd).save()
        messages.success(request,'The new user '+request.POST['Username']+" is registered successfully")
    return render(request,'Registration.html')

def loginpage(request):
    if request.method=="POST":
        try:
            Userdetails=Newuser.objects.get(Email=request.POST['Email'],Passwrd=request.POST['Passwrd'])
            print("Username=",Userdetails)
            request.session['Email']=Userdetails.Email
            results=Exam.objects.all()
            return render(request,'index.html',{"Exam":results})
        except Newuser.DoesNotExist as e:
            messages.success(request,'Username/Password Invalid')
    return render(request,'login.html')

def logout(request):
    try:
        del request.session['Email']
    except:
        pass
    return render(request,'index.html')



def adminpage(request):
    if request.method=='POST':
        Question=request.POST['Question']
        Option1=request.POST['Option1']
        Option2=request.POST['Option2']
        Option3=request.POST['Option3']
        Option4=request.POST['Option4']
        Answer=request.POST['Answer']


        Exam(Question=Question,Option1=Option1,Option2=Option2,Option3=Option3,Option4=Option4,Answer=Answer).save()
        messages.success(request,'Question Added Successfully...!')
    return render(request,'Admin.html')