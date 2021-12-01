from django.shortcuts import render,redirect
from django import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from .forms import *

def index(request):
    signupform = UserRegistrationForm()
    loginform = UserLoginForm()
    if request.method == "POST":
        if 'signupform' in request.POST:
            signupform=UserRegistrationForm(request.POST)
            if signupform.is_valid():
                signupobj=signupform.cleaned_data
                username=signupobj['username']
                email=signupobj['email']
                password=signupobj['password']
                User.objects.create_user(username=username, email=email, password=password)
        if 'loginform' in request.POST:
            loginform=UserLoginForm(request.POST)
            if loginform.is_valid():
                loginobj=loginform.cleaned_data
                username=loginobj['username']
                password=loginobj['password']
                user=authenticate(username=username,password=password)
                if user is None:
                    loginform.add_error('password','Invalid password')
                else:
                    login(request,user)
    context={}
    if signupform.errors:
        for field in signupform.errors:
            # print(signupform.errors[field])
            context[f'{field}']=signupform.errors[field]
    elif loginform.errors:
        for field in loginform.errors:
            context[f'{field}']=loginform.errors[field]
    # if request.user.is_authenticated:
        # print('logged')
    signupform = UserRegistrationForm()
    loginform = UserLoginForm()
    request.POST= None 
    return render(request,'index.html',context)

def logout_view(request):
    logout(request)
    url= request.GET.get('url')
    return redirect(url)