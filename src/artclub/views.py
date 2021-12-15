from django.shortcuts import render,redirect
from django import forms
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.contrib.auth.models import User

from cart.views import no_of_contents

from .forms import *

def index(request):
    data ={}
    data['no_of_contents']= no_of_contents(request.user)
    return render(request,'index.html',data)

def signup_view(request):
    signupform = UserRegistrationForm()
    if request.method == "POST":
        # print("data2")
        signupform=UserRegistrationForm(request.POST)
        if signupform.is_valid():
            # print("data3")
            signupobj=signupform.cleaned_data
            username=signupobj['username']
            email=signupobj['email']
            password=signupobj['password']
            User.objects.create_user(username=username, email=email, password=password,first_name=username)
    data={}
    if signupform.errors:
        data['valid']=False
        for field in signupform.errors:
            # print(signupform.errors[field])
            data[f'{field}']=signupform.errors[field]
    else:
        data['valid']=True
    # print("data = " , data)
    return JsonResponse(data)

def login_view(request):
    loginform = UserLoginForm()
    if request.method == "POST":
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
    data={}
    if loginform.errors:
        data['valid']=False
        for field in loginform.errors:
            data[f'{field}']=loginform.errors[field]
    else:
        data['valid']=True
    return JsonResponse(data)


def logout_view(request):
    logout(request)
    url= request.GET.get('url')
    return redirect(url)

def prints(request):
    return render(request,'prints.html',{})

def cart(request):
    return render(request,'cart.html',{})
