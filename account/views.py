from django.shortcuts import render,redirect
from account.forms import RegisterForm,LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from myapp.views import home
from django.urls import reverse



# Create your views here.


# def register(request):
#     form = RegisterForm()
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             if form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
#                 messages.error(_(request,"Password fields don't match"))
#             else:
#                 user = User.objects.create_user(
#                     username=form.cleaned_data['username'],
#                     email=form.cleaned_data['email'],
#                     password=form.cleaned_data['password'],
#                     confirm_password=form.cleaned_data['confirm_password']
#                 )
#                 user.save()
#                 messages.success(_(request,f'Account created for {user.username}!!'))
#                 return redirect('user_account:login')
#         return messages.error(request,_('Registration failed, Enter correct details'))
#     form=RegisterForm()
#     return render(request,'auth/register.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password != confirm_password:
                messages.error(request, _("Password fields don't match"))
            else:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],  # Use the cleaned password
                )
                user.save()
                messages.success(request, f'Account created for {user.username}!!')
                return redirect('accounts:login')
        else:
            messages.error(request, _('Registration failed. Please enter correct details.'))
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    form = LoginForm()
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                user.save() 
                messages.success(request, _( "You have logged in Successfully!"))
                return redirect(reverse('todo:home'))
            else:
                messages.error(request, _("Invalid Email or Password Provided"))
        form=LoginForm(request.POST)
    return render(request,'auth/login.html',{'form':form})



def logout_view(request):
    logout(request)
    return render(request,'auth/logout.html')

