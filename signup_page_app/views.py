from django.shortcuts import render ,redirect
from .models import * 
from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password

def signup_view(request):
    try:
    
        if request.method == 'POST':
            error =" "
            form = Signup_form(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                confirmpassword =form.cleaned_data['confirmpassword']
                if password == confirmpassword:
                    obj1 = User.objects.create(username=username, email=email, password=password)
                    sign = Signup.objects.create(user_id=obj1)
                    obj1.set_password(password)
                    obj1.save()
                    sign.save()
                    login(request, obj1)
                    return render(request, 'signup_page_app/logged.html', {'form': form})
                else:
                    error = 'Password not match'
            return render(request, 'signup_page_app/signup.html',{'form':form, 'error':error})            
        else:
            form = Signup_form()
            return render(request, 'signup_page_app/signup.html', {'form': form})  
    
    except Exception as e:
        print (str(e))
        return HttpResponse(str(e))
           


def login_View(request):
    try:
        if request.method == 'POST':
            form = Login_form(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = User.objects.get(username=username)
                if not user:
                    error = "User not exists"
                else:
                    if check_password(password, user.password):
                        login(request, user)
                        return render(request, 'signup_page_app/logged.html', {'form': form})
                    else:
                        error = "Password not match"
                        return render(request, 'signup_page_app/login.html', {'form': form, 'error': error})
            return render(request, 'signup_page_app/login.html', {'form': form, 'error': error})
        else:
            if request.user.is_authenticated():
                return render(request, 'signup_page_app/logged.html', {'form': form})
            else:
                form = Login_form()
                return render(request, 'signup_page_app/login.html', {'form': form})
    except User.DoesNotExist:
        form = Login_form()
        error = "user DoesNotExist"
        return render(request, 'signup_page_app/login.html', {'form': form, 'error': error})
    except Exception as e:
        form = Login_form()
        error = "Something went wrong"
        print(e)
        return render(request, 'signup_page_app/login.html', {'form': form, 'error': error})
        

def user_logout(request):
    logout(request)
    return redirect('/Form/login')      


