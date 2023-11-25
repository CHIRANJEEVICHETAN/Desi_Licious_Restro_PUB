from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages
from .models import bookTable, ContactUS, SubEmail

# Create your views here.
def index(request):
    if request.method == "POST":
        if 'tableName' in request.POST:  # Check if reservation form is submitted
            Tname = request.POST['tableName']
            Temail = request.POST['tableEmail']
            Tphone = request.POST['tablePhone']
            Tdate_str = request.POST['date']
            Ttime = request.POST['time']
            Tpeople = request.POST['people']
            Tmessage = request.POST['message']

            try:
                parsed_date = datetime.strptime(Tdate_str, "%d/%m/%Y").strftime("%Y-%m-%d")
            except ValueError:
                messages.error(request, "Invalid date format. Please use DD/MM/YYYY.")
                return redirect('index')  # Redirect back to the reservation form

            Tuser = bookTable(
                Tname=Tname, Temail=Temail, Tphone=Tphone, Tdate=parsed_date,
                Ttime=Ttime, Tpeople=Tpeople, Tmessage=Tmessage
            )
            Tuser.save()

            # Redirect to a success page or display a success message
            messages.success(request, "Reservation successfully submitted!")
            return redirect('index')  # Replace 'success_page' with the actual name/url of your success page

        elif 'ContactName' in request.POST:  # Check if contact form is submitted
            Cname = request.POST['ContactName']
            Cemail = request.POST['ContactEmail']
            Csub = request.POST['subject']
            Cmessage = request.POST['ContactMessage']
            Cuser = ContactUS(ContactName=Cname, ContactEmail=Cemail, subject=Csub, ContactMessage=Cmessage)
            Cuser.save()
            
            messages.success(request, "We will contact you soon!")
            return redirect('index')
        elif 'subEmail' in request.POST:
            Semail=request.POST['subEmail']
            Suser = SubEmail(email=Semail)
            Suser.save()

    return render(request, 'index.html')
def login(request):
    if request.method=="POST":
        un=request.POST['userName']
        ema=request.POST['emailLogin']
        pwd=request.POST['pass']
        user=auth.authenticate(username=un,email=ema,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('indexLogin')
        else:
            messages.info(request,'Invalid Credentials')
    return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        un=request.POST['userName']
        ema=request.POST['emailSignUP']
        pwd1=request.POST['pass1']
        pwd2=request.POST['pass2']
        if pwd1==pwd2:
            if User.objects.filter(username=un).exists():
                messages.info(request,'Username already exists')
                return render(request,'SignUp.html')
            elif User.objects.filter(email=ema).exists():
                messages.info(request,'Email already exists')
                return render(request,'SignUp.html')
            else:
                user=User.objects.create_user(username=un,email=ema,password=pwd2)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password does not match")
    else:
        return render(request,'SignUp.html')

    return render(request,'SignUp.html')

def termsOfServices(request):
    return render(request,'TermsOfservices.html')

def indexLogin(request):
    return render(request,'index_login.html')