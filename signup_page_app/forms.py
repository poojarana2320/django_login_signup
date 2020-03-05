from django import forms
from django.forms import TextInput
from .models import *
from django.contrib.auth.models import User

""" Signup form """


class Signup_form(forms.Form):
    username = forms.CharField(label="UserName", widget=forms.TextInput(attrs={'class': 'form_input'}))
    email = forms.EmailField(label="Email-id", widget=forms.TextInput(attrs={'class': 'form_input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_input'}))
    confirmpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_input'}))
    

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('A user has already registered using this email')
        return email


class Login_form(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form_input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_input'}))

