from .functions import update,balcheck,allaccounts
from django.contrib.auth.models import User

def okoapay(request,value):
    debt=float(balcheck(request,"okoataken"))
    if debt>0:
        if debt<=value:
            value-=debt
            message=f"{debt} bob has been deducted to repay your okoa debt. Your debt is fully repaid"
            debt=0
        else:
            debt-=value
            message=f"{value} bob has been deducted to repay your okoa debt. Check your remaining debt"
            value=0
        update(request,{"okoataken":debt})
        return {"value":value,"message":message}
    return {"value":value}



def okoatake(request,data=0):
    okoalimit=int(allaccounts(request.user).get('okoalimit'))
    okoa_taken=int(allaccounts(request.user).get("okoataken"))
    okoa_bal=int(allaccounts(request.user).get("okoabal"))
    limits=[limit for limit in range(10,30,10)]+[limit for limit in range(50,int(okoalimit)+10,50)]
    if data==0:
        return {"limits":limits,"okoalimit":okoalimit,"okoataken":okoa_taken}
    else:
        okoatake=float(request.POST.get("okoatake"))
        if okoatake>okoalimit or okoatake>okoalimit-okoa_taken: return "please take a lower amount"
        elif okoalimit<=0:return "You are not eligible for this service now"
        else:
            okoa_taken+=okoatake
            okoa_bal+=okoatake
            update(request,{"okoataken":okoa_taken,"okoabal":okoa_bal})
            return f'you have been credited with {okoatake}'


class Sambaza():
    def __init__(self,recpnum):
        self.user=recpnum

def checknum(recpnum):
    if not User.objects.filter(username=recpnum).count():return False
    else: return True

def airtimebal(request,value):
    okoalimit=float(balcheck(request,"okoalimit"))
    airtime=float(balcheck(request,"airtime"))
    pay=okoapay(request,value)
    airtime+=pay.get("value")
    message=pay.get("message")
    if airtime*1.5>okoalimit:okoalimit=airtime*1.5
    update(request,{"airtime":airtime,"okoalimit":okoalimit})

def recharge(request):
    bob10=["12345","12354","12435","12453","12534","12543","13245","13254"]
    bob20=["13425","13452",'13524',"13542","14235","14253","14235","14352"]
    bob50=["14523","14532","15234","15243","15324","15342","15423","15432"]
    code=request.POST.get('scratch')
    if code in bob10:value=10
    elif code in bob20:value=20
    elif code in bob50:value=50
    else:value=0
    if value==0:text="The voucher does not exist"
    else: text=f'Recharge of {value} was successfull'
    if request.POST.get('recpnum'):
        recpnum=request.POST.get('recpnum')
        request=Sambaza(recpnum)
        if not checknum(recpnum):
            raise ValueError("The Number you entered does not exist")  
    airtimebal(request,value)