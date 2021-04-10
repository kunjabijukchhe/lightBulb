from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import pyrebase
firebaseConfig = {
    'apiKey': "AIzaSyDj-epa6wHzWuxTqKIINk2d1zaE0RoyQD4",
    'authDomain': "apps-adccc.firebaseapp.com",
    'databaseURL': "https://apps-adccc-default-rtdb.firebaseio.com",
    'projectId': "apps-adccc",
    'storageBucket': "apps-adccc.appspot.com",
    'messagingSenderId': "468281552905",
    'appId': "1:468281552905:web:5ab99a52c80977acdc08d8",
    'measurementId': "G-H9YMW1C8P3"
}
firebase=pyrebase.initialize_app(firebaseConfig);
db=firebase.database()

def update(request):
    a=db.child('bulb').update({'lightOne':'False'})
    return render(request,'dashboardOne.html',{'a':a})

@login_required
def index(request):
    return render(request,'button.html')

def login_view(request):
 
    if request.method=="POST":
        user_name=request.POST.get('username')
        pass_word=request.POST.get('password')
        user=authenticate(username=user_name,password=pass_word)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('lightApp:button'))
            else:
                return HttpResponse('Account is not Active')
        else:
            print('someone tried to login and failed')
            print('Username:{} and Password:{}'.format(user_name,pass_word))
            return HttpResponse("Invalid Username and Password")
    else:
        return render(request,'login.html')
        
@login_required
def logout_view(request):
    logout(request)
    return redirect("login")
   
@login_required
def dashboard(request):
    return render(request,'dashboardOne.html')
    # return render(request,'dashboard.html')