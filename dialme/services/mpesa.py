from django.shortcuts import render
from .functions import update,balcheck
from users.models import Regusers
from .topup import Sambaza,checknum,airtimebal
from .models import Statement
from accounts.models import Agent

def checkpin(request):
    user=Regusers.objects.filter(user_num=request.user)
    pin=list(user.values("mpin"))[0].get("mpin")
    if request.POST.get("mpin")==pin:
        return True

def balancecheck(request,cost):
    mpesa=balcheck(request,"mpesa")
    if cost>mpesa: return False
    else: return True
def agentcheck(agentnum):
    if Agent.objects.filter(agentnum=agentnum).count():return True

def codegenerator():
    import string,random
    pool=[str(a) for a in range(10)]+list(string.ascii_uppercase)
    p=[]
    for a in range(10):
        p.append(random.choice(pool))
    code="".join(p)
    return code

def confirmpin(request,message):
   return render(request,'services/mpesa.html',{"mpesa":balcheck(request,'mpesa'),"mpesaoption":"sendmoney","message":message,"mpinrequired":True})

def statement(details,Commit=True):
        transaction=details.get("transaction")
        tx=Statement.objects.create(
        code=details.get("code"),
        user_num=details.get("user"),
        transaction=transaction,
        amount=details.get("amount"),
        trans_cost=details.get("trans_cost"))
        tx=Statement.objects.get(code=details.get("code"))
        if transaction=="Withdraw":tx.agent=details.get("agent")
        elif transaction=="Send money":tx.recipient=details.get("recipient")
        elif transaction=="Pay bill":
            tx.paybill=details.get("paybill")
            tx.account=details.get("account")
        tx.save()

def tx_cost(tx,amount)           :
    if tx=="withdraw" :
        if amount<=100:cost=10
        elif amount<=1000:cost=27
        elif amount<=10000:cost=50
        else:cost=100
    else:
        if amount<=100:cost=0
        elif amount<=1000:cost=10
        elif amount<=10000:cost=20
        else:cost=50
    return cost

def sendmoney(request):
    tempreq=request
    if request.method=="POST":
        if not request.POST.get("mpin"):
        
            recpnum=request.POST.get("recpnum")
            amount= float(request.POST.get("sendamount"))
            cost=tx_cost("send",amount)
            if not checknum(recpnum):
                return render(request,'services/mpesa.html',{"mpesa":balcheck(request,'mpesa'),"mpesaoption":"sendmoney","message":"error"})
            recipient=Regusers.objects.get(user_num=recpnum)
            if balancecheck(request,amount+cost):
                message=f'Send Kshs.{amount} to {recipient.first_name} {recipient.last_name} . Transaction cost:{cost}'
                return render(request,'services/mpesa.html',{"mpesa":balcheck(request,'mpesa'),"mpesaoption":"sendmoney","message":message,"mpinrequired":True,"form":request.POST})
            return render(request,'services/mpesa.html',{"mpesa":balcheck(request,'mpesa'),"mpesaoption":"sendmoney","message":"error"})
        if request.POST.get("option")=="cancel": return render(request,'services/mpesa.html',{"mpesa":balcheck(request,'mpesa'),"mpesaoption":"sendmoney","form":request.POST})

        if checkpin(request):   
            recpnum=request.POST.get("recpnum")
            amount= float(request.POST.get("sendamount"))  
            cost=tx_cost("send",amount)   
      
            mpesa=balcheck(request,"mpesa")-(amount+cost)
            update(request,{"mpesa":mpesa})
            code=codegenerator()
            statement({"code":code,"recipient":recpnum,"amount":amount,"user":request.user,"transaction":"Send money","trans_cost":cost})

            request=Sambaza(recpnum)
            mpesa=balcheck(request,"mpesa")+amount
            update(request,{"mpesa":mpesa})
            request=tempreq
            
        return render(request,'services/mpesa.html',{"mpesa":balcheck(request,'mpesa'),"mpesaoption":"sendmoney","message":"error"})
    return render(request,'services/mpesa.html',{"mpesa":balcheck(request,'mpesa'),"mpesaoption":"sendmoney"})

def withdraw(request):
    tempreq=request
    if request.method=="POST":
        if not request.POST.get("mpin"):
            agentnum=request.POST.get("agentnum")
            amount= float(request.POST.get("withamount"))
            cost=tx_cost("withdraw",amount)
            if not agentcheck(agentnum):
                return render(request,'services/mpesa.html',{"mpesa":balcheck(request,'mpesa'),"mpesaoption":"withdraw","message":"error"})
            agent=Agent.objects.get(agentnum=agentnum)
            if balancecheck(request,amount+cost):
                message=f'Withdraw Kshs.{amount} from {agent.agentname}. Transaction cost:{cost}'
                return render(request,'services/mpesa.html',{"mpesa":balcheck(request,'mpesa'),"mpesaoption":"withdraw","message":message,"mpinrequired":True,"form":request.POST})
            return render(request,'services/mpesa.html',{"mpesa":balcheck(request,'mpesa'),"mpesaoption":"withdraw","message":"error"})
        
        if checkpin(request):
            agent=request.POST.get("agentnum")
            amount= float(request.POST.get("withamount"))        
            cost=tx_cost("withdraw",amount)   
            mpesa=balcheck(request,"mpesa")-(amount+cost)
            update(request,{"mpesa":mpesa})
            code=codegenerator()
            statement({"code":code,"agent":agent,"amount":amount,"user":request.user,"transaction":"Withdraw","trans_cost":cost})
            
            
        return render(request,'services/mpesa.html',{"mpesa":balcheck(request,'mpesa'),"mpesaoption":"withdraw","message":"error"})
    return render(request,'services/mpesa.html',{"mpesa":balcheck(request,'mpesa'),"mpesaoption":"withdraw"})


def paybill(request):
    pass

def airtime(request):
    if request.method=="POST":
        tempreq=request
        if not request.POST.get("mpin"):
            
            amount= float(request.POST.get("amount"))
            payable= balancecheck(request,amount)
            if request.POST.get("recpnum"):
                recpnum=request.POST.get("recpnum")
                if not checknum(recpnum):
                    return render(request,'services/mpesa.html',{"mpesa":balcheck(request,'mpesa'),"mpesaoption":"sendmoney","error":"The number doesn't exist"})
                recipient=Regusers.objects.get(user_num=recpnum)
                if payable:
                    message=f'buy airtime of Kshs.{amount} for {recipient.first_name} {recipient.last_name}'
            else:
                recpnum=""
                message=f'buy airtime of Kshs.{amount} for me'
            return render(request,'services/mpesa.html',{"mpesa":balcheck(request,'mpesa'),"mpesaoption":"buy airtime","message":message,"mpinrequired":True,"form":request.POST})
        if checkpin(request):   
            amount= float(request.POST.get("amount")) 
            mpesa=balcheck(request,"mpesa")-amount
            recpnum=request.POST.get("recpnum")
            update(request,{"mpesa":mpesa})
            code=codegenerator()
            statement({"code":code,"recipient":recpnum,"amount":amount,"user":request.user,"transaction":"buy airtime","trans_cost":0})
            if request.POST.get("recpnum"):
                request=Sambaza(recpnum)
            airtimebal(request,amount)              
            request=tempreq
         
            
        return render(request,'services/mpesa.html',{"mpesa":balcheck(request,'mpesa'),"mpesaoption":"buy airtime","error":"error"})
    return render(request,'services/mpesa.html',{"mpesa":balcheck(request,'mpesa'),"mpesaoption":"buy airtime"})



    