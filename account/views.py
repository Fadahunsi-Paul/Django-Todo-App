from django.shortcuts import render
from account.forms import RegistrationForm,LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



# Create your views here.

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            confirm_password=form.cleaned_data.get('confirm_password')
            if password != confirm_password:
                raise HttpResponse("Password Don't Match")
            user=form.save()
    form=RegistrationForm()
    return render(request,'auth/register.html',{'form':form})


def login_view(request):
    form = LoginForm()
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email=from.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            user=authenticate(email=email,password=password)
            if user:
                login(request,user)
                messages.success(request, "You have logged in Successfully!")
                return redirect('todo:home')
            messages.error(request,"Invalid Username or Password")
    form=LoginForm(request.POST)
    return render(request,'auth/login.html',{'form':form})


def logout_view(request):
    logout(request)
    return render(request,'auth/logout.html')

