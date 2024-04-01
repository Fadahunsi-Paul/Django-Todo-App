from django import forms 
from django.contrib.auth.models import User 
from django.forms import ModelForm

class RegisterForm(forms.ModelForm):
    username = forms.CharField(required=True,
    widget = forms.TextInput(
        attrs={
            'placeholder':'Enter Username',
            'class':'form-control'
        }
    )) 

    email=forms.EmailField(required=True,
    widget = forms.TextInput(
        attrs={
            'placeholder':'Enter Email',
            'class':'form-control'
        }
    ))

    password=forms.CharField(required=True,
    widget = forms.TextInput(
        attrs={
            'placeholder':'Enter Password',
            'class':'form-control'
        }
    ))

    confirm_password=forms.CharField(required=True,
    widget = forms.TextInput(
        attrs={
            'placeholder':'Re-enter Password',
            'class':'form-control'
        }
    ))
    class Meta:
        model= User
        fields=['username','email','password']


class LoginForm(forms.ModelForm):
    email=forms.EmailField(required=True,
    widget = forms.TextInput(
        attrs= {
            'placeholder':'Enter Email',
            'class':'form-control'
        }
    ))

    password=forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter Password',
                'class':'form-control'
            }
        )
    )

    
    class Meta:
        model= User
        fields=['email','password']