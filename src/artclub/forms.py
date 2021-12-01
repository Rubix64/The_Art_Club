from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=30,required=True)
    email = forms.EmailField(max_length=75,required=True)
    password = forms.CharField(max_length=50,required=True,widget=forms.PasswordInput)
    confirmpassword = forms.CharField(max_length=50,required=True,widget=forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            self.add_error('username','Username already exists')

        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            self.add_error('email','Email already exists')

        password = self.cleaned_data['password']
        confirmpassword=self.cleaned_data['confirmpassword']
        if password != confirmpassword:
            self.add_error('password',"Passwords must match")
        return super(UserRegistrationForm,self).clean()

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30,required=True)
    password = forms.CharField(max_length=50,required=True,widget=forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username).exists():
            self.add_error('username',"Username doesn't exist")

        password = self.cleaned_data['password']
        # if password != User.objects.filter(username=username).only('password'):
        #     self.add_error('password',"Invalid Password")
        return super(UserLoginForm,self).clean()
