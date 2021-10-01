from accounts.models import Accounts
from users.models import Regusers

def allaccounts(user):
    acc=acc=Regusers.objects.get(user_num=user)
    accounts=acc.accounts
    airtime=accounts.airtime
    bonga=accounts.bonga
    bundles=accounts.bundles
    sms=accounts.sms
    mpesa=accounts.mpesa
    okoa_bal=accounts.okoa_bal
    okoa_taken=accounts.okoa_taken
    okoa_limit=accounts.okoa_limit

    accounts={"airtime":airtime,"bonga":bonga,"sms":sms,"bundles":bundles,"mpesa":mpesa,"okoabal":okoa_bal,"okoalimit":okoa_limit,"okoataken":okoa_taken}
    return accounts


def balcheck(request,balname):

    user=request.user
    return allaccounts(user).get(balname)
def update(request,bals):
    user=request.user
    acc=Regusers.objects.get(user_num=user)
    for balname in bals.keys():
        value=bals.get(balname)
        if balname=="airtime":acc.accounts.airtime=value
        elif balname=="bonga":acc.accounts.bonga=value
        elif balname=="bundles":acc.accounts.bundles=value
        elif balname=="sms":acc.accounts.sms=value
        elif balname=="okoabal":acc.accounts.okoa_bal=value
        elif balname=="okoalimit":acc.accounts.okoa_limit=value
        elif balname=="okoataken":acc.accounts.okoa_taken=value
        elif balname=="mpesa":acc.accounts.mpesa=value
        else:pass
        acc.accounts.save()



def costcalculator(request,cost):
    airtime=float(balcheck(request,"airtime"))
    okoabal=float(balcheck(request,"okoabal"))
    if cost>okoabal+airtime: return "insufficient airtime"
    if okoabal>=cost:okoabal-=cost
    else:
        cost-=okoabal
        airtime-=cost
        okoabal=0
    update(request,{'okoabal':okoabal,"airtime":airtime})
    return 1
    
