from django.http import HttpResponse
from django.shortcuts import render,redirect
from Technician.forms import Bookfrom
from django.contrib.auth.models import User
from account.models import Lab
from Technician.models import Test,booking,Report,booking
from Technician.forms import Reportform
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import authenticate ,login as authlog ,logout as authlogout
# Create your views here.
def login(request):
    context={"title":"User Login","ff":"good"}
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
                return redirect("/vbranch")
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

def register(request):
    context={}
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:

            context["form"]=UserCreationForm(request.POST)
            return render(request,"user/form.html",context=context)

    else :
        context["form"]=UserCreationForm()
        return render(request,"user/form.html",context=context)

def book_test(request,id):
    userid=request.user.id
    user=User.objects.get(id=userid)
    test=Test.objects.get(id=id)
    context={"test":test}
    if request.method=="POST":
        date=request.POST["date"]
        book=booking.objects.create(user=user,test=test,date=date,token=12)
        b=book.save()

        return redirect("/viewb/"+str(book.id))
    else :
        return render(request,"user/book.html",context=context)

            
def view_branch(request):
    lab=Lab.objects.all()
    context={"branch":lab}
    context['home']=1
    return render(request,"user/branch.html",context)

def view_test(request,id):
    test=Test.objects.filter(lab_id=id)
    context={"test":test}
    return render(request,"user/test.html",context)


def viewstatus(request,id):
    book=booking.objects.get(id=id)
    return HttpResponse(book.status)

def vsample(request):
    return render(request,"index.html")

def viewbooking(request,id):
    book=booking.objects.get(id=id)
    context={"i":book}
    if book.status=="approve":
        context["approve"]=True
    return render(request,"user/viewbook.html",context=context)

def logout(request):
    authlogout(request)
    return redirect("/")

def allbook(request):
    book=booking.objects.filter(user_id=request.user.id)
    context={"book":book}
    return render(request,"user/allbook.html",context)

def viewreport(request):
    userid=request.user.id
    if not Report.objects.filter(user_id=userid).exists():
        context={"message":"No reporters for you"}
        return render(request,"user/report.html",context=context)
    else:
        context={"report":Report.objects.filter(user_id=userid)}
        return render(request,"user/report.html",context=context)
def reportdetails(request,id):
    r=Report.objects.get(id=id)
    context={"i":r}
    return render(request,"user/reportdetials.html",context=context)
    