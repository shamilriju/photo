from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid details')
            return redirect('/')
    else:
        return render(request,"login.html")

def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username used')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,password=password, email=email)
                user.save()
                print("done")
        else:
            messages.info(request, 'password not match')
            return redirect('register')
        return redirect('home')
    return render(request,"register.html")