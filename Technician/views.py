from django.shortcuts import render

# Create your views here.
from symbol import pass_stmt
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate ,login as authlog,logout as authlogout
from Technician.models import Test, booking,Report,Token
from account.models import Lab, Tech 
from django.http import HttpResponse
from .forms import Testforms,Reportform
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def logout(request):
    authlogout(request)
    return redirect("/tech/login")

def login(request):
    context={"title":"Technician Login"}
    if request.method=="POST":
        user=request.POST["username"]
        print(user)
        password=request.POST["password"]
        print(password)
        if user and password:
            usob=authenticate(request,username=user,password=password)
            print(usob)
            if usob:
                authlog(request,usob)
                return redirect("/tech/addtest")
            else :
                context["message"]="Wrong Username or password"
                context["form"]=AuthenticationForm()
                return render(request,"lo.html",context=context)
        else :
            context["message"]="please enter the username and password"
            context["form"]=AuthenticationForm()
            return render(request,"lo.html",context=context)
    else:
        context["form"]=AuthenticationForm()
        return render(request,"lo.html",context=context)
        
def viewtest(request):
    context={}
    userid=request.user.id
    tech=Tech.objects.get(user_id=userid)
    lab=Lab.objects.get(id=tech.lab.id)
    test=Test.objects.filter(lab=lab)
    context["test"]=test
    return render(request,"viewtest.html",context=context)

def addtest(request):
    context={"title":"Add test","type":"time","id":"id_duration"}
    userid=request.user.id
    tech=Tech.objects.get(user_id=userid)
    lab=Lab.objects.get(id=tech.lab.id)
    context['form']=Testforms()
    if request.method=="POST":
        form=Testforms(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.lab=lab
            data.save()
            context["message"]="saved"
            return render(request,"form.html",context=context)
        else:
            context["message"]="not saved"
            return render(request,"form.html",context=context)
    else:
        return render(request,"form.html",context=context)

def edittest(request,id):
    context={"title":"Edit test"}
    test=Test.objects.get(id=id)
    userid=request.user.id
    tech=Tech.objects.get(user_id=userid)
    lab=Lab.objects.get(id=tech.lab.id)
    context['form']=Testforms(instance=test)
    if request.method=="POST":
        form=Testforms(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.lab=lab
            data.save()
            context["message"]="data updated"
            return render(request,"form.html",context=context)
        else:
            context["message"]="not valid"
            return render(request,"form.html",context=context)
    else:
        return render(request,"form.html",context=context)

def removetest(request,id):
    if Test.objects.filter(id=id).exists():
        test=Test.objects.get(id=id)
        test.delete()
        return redirect("/tech/vtest")
    else:
        return redirect("/tech/vtest")

def viewbooking(request):
    context={}
    lab=getlab(request.user.id)
    test=Test.objects.filter(lab=lab)
    testid=[]
    for i in test:
        testid.append(i.id)
    if not booking.objects.filter(test=tuple(testid),status="pending").exists():
        context["message"]="no booking"
    book=booking.objects.filter(test=tuple(testid),status="pending")
    context["title"]="Manage Request"
    context["book"]=book
    return render(request,"booking.html",context=context)

def approvebooking(request,id):
    book=booking.objects.get(id=id)
    book.status="approve"
    book.token=generatetoken(book.date,book.test.lab);
    book.save()
    return redirect("/tech/viewbooking/")

def rejectbooking(request,id):
    book=booking.objects.get(id=id)
    book.status="reject"
    book.save()
    return redirect("/tech/viewbooking/")
    
def getreadyforbooking(id):
    pass

def getlab(userid):
    usrid=userid
    tech=Tech.objects.get(user_id=usrid)
    return Lab.objects.get(tech=tech)

def add_report(request,id):
    test=booking.objects.get(id=id)

    context={"form":Reportform(),"title":"Add report","type":"date","id":"id_compltedate"}
    if request.method == "POST":
        form=Reportform(request.POST)
        if form.is_valid():
                data=form.save(commit=False)
                data.test=test
                data.givendate=test.date
                data.user=test.user
                data.save()
                return HttpResponse("saved")
        else:
            return HttpResponse("not valid")
    else:
        print("hoi")
        return render(request,"form.html",context=context)

def remove_report(request,id):
    lab=Lab.objects.get(id=id)
    lab.delete()
    return HttpResponse("removed")

def edit_report(request,id):
    re=Report.objects.get(id=id)
    context={"form":Reportform(instance=re)}
    if request.method == "POST":
        form=Reportform(request.POST)
        if form.is_valid():
                data=form.save(commit=False)
                data.save()
                return HttpResponse("saved")
        else:
            return HttpResponse("not valid")
    else:
        return render(request,"form.html",context=context)

def generatetoken(date,lab):
    if Token.objects.filter(date=date,lab=lab).exists():
        to=Token.objects.get(date=date,lab=lab);
        count=to.current_token
        to.current_token=count+1;
        to.save()
        return count;
    else :
        Token.objects.create(date=date,lab=lab,current_token=1)
        return 1;

def vreport(request):
    context={}
    lab=getlab(request.user.id)
    test=Test.objects.filter(lab=lab)
    testid=[]
    for i in test:
        testid.append(i.id)
    if not booking.objects.filter(test=tuple(testid),status="approve").exists():
        context["message"]="no booking"
    book=booking.objects.filter(test=tuple(testid),status="approve")
    context["book"]=book
    context["title"]="Manage report"
    return render(request,"viewreport.html",context=context)