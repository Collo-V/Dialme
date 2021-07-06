from django.shortcuts import render
from .models import Accounts

def accounts_view(request):
    accounts= Accounts.objects.all()[:4]+Accounts.objects.all()[-2:]
    return render(request,"accounts/sccounts.html",{'accounts':accounts})
# Create your views here.
