#from USSD.bundles import bundles

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .functions import *
from .topup import recharge,okoatake
from .bundles import *
from .mpesa import checkpin
# Create your views here.


def TopUp(request):
    if request.method=="POST":
        recharge(request)
    return render(request,'services/topup.html',)
    
    
def Okoa(request):
    okoabals=okoatake(request)
    if request.method=="POST":
        message=okoatake(request,data=1)
        return render(request,'services/topup.html',{'okoabals':okoabals,"message":message})
    else:
        return render(request,'services/topup.html',{'okoabals':okoabals})
    
@login_required(login_url="/users/login")       
def Bundles(request):
    balances=allaccounts(request.user)
    bundleoptions=databundles()
    if request.method=="POST":
        message=databundles(request)
        return render(request,'services/bundles.html',{'bundleoptions':bundleoptions,"airtime":balances.get('airtime'),"message":message})
    else:
        return render(request,'services/bundles.html',{'bundleoptions':bundleoptions,"airtime":balances.get('airtime')})
    
def SMS(request):
    smsoptions=smsbundles()
    if request.method=="POST":
        smsbundles(request)
    else:
        balances=allaccounts(request.user)
    return render(request,'services/bundles.html',{'smsoptions':smsoptions,"airtime":balcheck(request,'airtime')})
    

def Bonga(data):
    pass
def Mpesa(request):
    if request.method=="POST":
        if request.POST.get("option")=="checkbal":
            if checkpin(request):
                return render(request,'services/mpesa.html',{"mpesa":balcheck(request,'mpesa')})
        else:options(request)
        return render(request,'services/mpesa.html',{"mpesa":balcheck(request,'mpesa')})


    
    return render(request,'services/mpesa.html',{"mpesa":balcheck(request,'mpesa')})
@login_required(login_url="/users/login")
def services(request):


    services={'TopUp':TopUp,"Okoa":Okoa,'Bundles':Bundles,"SMS":SMS,'Bonga':Bonga,'Mpesa':Mpesa}
    skeys=services.keys()
    todo=""
    if request.method=="POST":
        serviceop=request.POST.get('serviceop')
        raise ValueError("again")
        tocall=services.get(serviceop)
        todo=tocall(request,data=1)
    try:
        balances=allaccounts(request.user)
    except:
        balances=""
        pass
    limits=Okoa(request)
   

    
    return render(request,'homepage.html',)
