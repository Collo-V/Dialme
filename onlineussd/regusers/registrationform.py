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
    username=forms.CharField(label="Enter the Number",max_length=10,min_length=10,widget=forms.TextInput(attrs={"class":"reginput","id":"usernum"}))
    first_name=forms.CharField(label="Enter Your First Name",min_length=4,max_length=15,widget=forms.TextInput(attrs={"class":"reginput","id":"fname"}))
    last_name=forms.CharField(label="Enter Your Last name",min_length=4,max_length=15,widget=forms.TextInput(attrs={"class":"reginput","id":"lname"}))
    password1=forms.CharField(min_length=8, label="Enter the password",widget=forms.PasswordInput(attrs={"class":"reginput","id":"password1"}))
    password2=forms.CharField(min_length=8,label="Confirm Password",widget=forms.PasswordInput(attrs={"class":"reginput","id":"password1"}))
    mpin1=forms.CharField(label="Set an mpesa PIN",min_length=4,max_length=4,widget=forms.PasswordInput(attrs={"class":"reginput","id":"mpin1"}))
    mpin2=forms.CharField(label="Confirm PIN",max_length=4,min_length=4,widget=forms.PasswordInput(attrs={"class":"reginput","id":"mpin2"}))
    #regdate=forms.DateTimeField(widget=forms.HiddenInput(default=datetime.datetime.now())
    
    


    def clean_user_num(self):
        
        username=self.cleaned_data.get('username')
        r=User.objects.filter(username=username)
        if r.count():raise ValidationError({"error":"Username already exists"})
        if len(username)>10 and len(username)<10:
            raise ValidationError({"The number must be 10 digits long"})
        try:username=str(username)
        except:raise ValidationError({"The number must be digits"})
        return username


    def clean_password(self) :
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("The passwords do not match")
        return password2

    def clean_mpin(self):
        mpin1=self.cleaned_data.get("mpin1")
        mpin2=self.cleaned_data.get("mpin2")
        if mpin1 and mpin2 and mpin2!=mpin1:
           raise forms.ValidationError("The pins Do not match")
        return mpin1

    def cleans(self):
        self.is_valid()
        self.username=self.clean_user_num()
        self.password=self.clean_password()
        self.mpin=self.clean_mpin()
        return True

    

    def Reguser(self,reg,Commit=True):
        reguser=Regusers.objects.create(
        user_num=self.cleaned_data["username"],
        first_name=self.cleaned_data['first_name'],
        last_name=self.cleaned_data['last_name'],
        password=self.cleaned_data['password'] ,  
        mpin=self.cleaned_data["mpin"],
        )
        from accounts.models import Accounts
        Accounts.objects.create(
            reguser
        )
        return reguser
    

    def save(self, Commit=True):
        user=User.objects.create_user(
            self.cleaned_data['username'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            password=self.cleaned_data['password1'],
            
           
        )
        self.Reguser()
        return user

