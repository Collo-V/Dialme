from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .registrationform import userregistration
from django.contrib.auth import login,logout
import datetime
from django.urls import reverse

def registration(request):
    if request.method=="POST":
        form=userregistration(request.POST)
        
        if form.cleans():
            user=form.save()
            login(request,user)
            return redirect("services:homepage")
    else:form=userregistration()
    return render(request,'users/registration.html',{"form":form})


def signin(request):
    if request.method =="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get(next))
            else:
                return redirect(reverse('services:homepage'))
    else:
        form=AuthenticationForm()
    return render(request,'users/login.html',{'form':form})

def signout(request):
    if request.method=="POST":
        logout(request)
        return redirect('services:homepage')

