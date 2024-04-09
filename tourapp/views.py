from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import destination
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        print(first_name,last_name,username,password1,password2,email)
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exists")
                return render(request,'register.html')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return render(request,'login.html')
                
        else:
             messages.info(request,"password not matching")
             return render(request,'register.html')
        
    else:
        return render(request,'register.html')
def login(request):
    dests=destination.objects.all()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'index.html',{'username':username,'dests':dests})
        else:
            messages.info(request,"username doesn't exist")
            return redirect(login)

    else:
        return render(request,'login.html')
def index(request):
    dests=destination.objects.all()
    username = request.user.username 
    return render(request,'index.html',{'dests':dests,'username': username})
def about(request):
    username = request.user.username 
    return render(request,'about.html',{'username': username})
def contact(request):
    username = request.user.username 
    return render(request,'contact.html',{'username': username})
def services(request):
    username = request.user.username 
    return render(request,'services.html',{'username': username})
def base(request):
    return render(request,'base.html')

