from django.shortcuts import render
from testquiz.models import Exam
from testquiz.models import Newuser
from testquiz.models import QuizHistory

from django.contrib import messages
from datetime import datetime



def indexpage(request):
    return render(request,'index.html')

def examonline(request):
    
    results=Exam.objects.all()[1:5]
    
    if request.method=='POST':
        
        
        for i in range(0,4):

            Email=request.POST['Email']
            Question=request.POST['a'+str(i)]
            try:
                YourAnswer=request.POST[str(i+2)]
            except:
                YourAnswer='Not Selected'
            Answer=request.POST['Answer'+str(i)]

            QuizHistory(Email=Email,Question=Question,YourAnswer=YourAnswer,Answer=Answer,Time=datetime.now()).save()
        return render(request,'index.html') 

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
            return render(request,'index.html')
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


def history(request):
    try:
        AllHistory=QuizHistory.objects.filter(Email=request.session['Email'])
    except:
        return render(request,'History.html')
    try:

        sometime=AllHistory[0].Time
        someHist=[]
        for x in AllHistory:
            if x.Time==sometime:
                someHist.append(x)
        
        return render(request,'History.html',{"History":AllHistory,"someHist":someHist})
    except:
        messages.success(request,"no History found")
        return render(request,'History.html')
    