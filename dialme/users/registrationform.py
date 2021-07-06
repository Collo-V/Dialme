import datetime
from django.shortcuts import render
from .models import Regusers
from django.http import HttpResponse
from django.contrib.admin import autodiscover
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

from django import forms
from django.core.exceptions import ValidationError



class userregistration(forms.Form):
    username=forms.CharField(error_messages="",label="Enter the Number",max_length=10,min_length=10,widget=forms.TextInput(attrs={"class":"reginput","id":"usernum"}))
    first_name=forms.CharField(label="Enter Your First Name",min_length=4,max_length=15,widget=forms.TextInput(attrs={"class":"reginput","id":"fname"}))
    last_name=forms.CharField(label="Enter Your Last name",min_length=4,max_length=15,widget=forms.TextInput(attrs={"class":"reginput","id":"lname"}))
    password1=forms.CharField(min_length=8, label="Enter the password",widget=forms.PasswordInput(attrs={"class":"reginput","id":"password1"}))
    password2=forms.CharField(min_length=8,label="Confirm Password",widget=forms.PasswordInput(attrs={"class":"reginput","id":"password2"}))
    mpin1=forms.CharField(label="Set an mpesa PIN",min_length=4,max_length=4,widget=forms.PasswordInput(attrs={"class":"reginput","id":"mpin1"}))
    mpin2=forms.CharField(label="Confirm PIN",max_length=4,min_length=4,widget=forms.PasswordInput(attrs={"class":"reginput","id":"mpin2"}))
    #regdate=forms.DateTimeField(widget=forms.HiddenInput(default=datetime.datetime.now())
    
    


    def clean_user_num(self):
        
        username=self.cleaned_data.get('username')
        r=User.objects.filter(username=username)
        if r.count():return "Username already exists"
        if len(username)>10 and len(username)<10:
            self.username.error_messages="The number must be 10 digits long"
            return True
        try:username=int(username)
        except:return "The number must be digits"
        return False


    def clean_password(self) :
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        if password1 and password2 and password1!=password2:
            return "The passwords do not match"
        return False

    def clean_mpin(self):
        mpin1=self.cleaned_data.get("mpin1")
        mpin2=self.cleaned_data.get("mpin2")
        if mpin1 and mpin2 and mpin2!=mpin1:
           return "The pins Do not match"
        return False

    def cleans(self):
        self.is_valid()
        username={"error":self.clean_user_num()}
        password1={"error":self.clean_password()}
        mpin2={"error":self.clean_mpin()}
        if username["error"]==False and password1["error"]==False and mpin2["error"]==False: return True
        else: return {"username":username,"password1":password1,"mpin2":mpin2}

    

    def Reguser(self,Commit=True):
        reguser=Regusers.objects.create(
        user_num=self.cleaned_data["username"],
        first_name=self.cleaned_data['first_name'],
        last_name=self.cleaned_data['last_name'],
        password=self.cleaned_data['password1'] ,  
        mpin=self.cleaned_data["mpin1"],
        )
        from accounts.models import Accounts
        user=Accounts(reguser.user_num)
        user.save()
        return reguser
    

    def save(self, Commit=True):
        user=User.objects.create_user(
            self.cleaned_data['username'],
            first_name=self.cleaned_data['first_name'],
            password=self.cleaned_data['password1'],         
           
        )
        self.Reguser()
        return user

