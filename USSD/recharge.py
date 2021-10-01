import datetime
from accounts import *
from statements import statements
from notifications import notif_write


bob10=["12345","12354","12435","12453","12534","12543","13245","13254"]
bob20=["13425","13452",'13524',"13542","14235","14253","14235","14352"]
bob50=["14523","14532","15234","15243","15324","15342","15423","15432"]

def scratch_values(code):    
    if code in bob10:
        value = 10
    elif code in bob20:
        value=20
    elif code in bob50:
        value=50
    else:
        value=0
    return value




def recharge(number,value):
    okoa_taken=balance_check(number,"okoa_taken")
    airtime_bal=balance_check(number,"airtime")
    okoa_limit=balance_check(number,"okoa_limit")
    bonga_bal=balance_check(number,"bonga")
    bongapoints=int(value*20/100)
    initval=value
    if okoa_taken>0:
        if okoa_taken<=value:
            notif_write(number,okoa_taken,4)
            okoa_taken=0
            value-=okoa_taken
        else:
            notif_write(number,value,5)
            okoa_taken-=value
            value=0
    airtime_bal+=value
    bonga_bal+=bongapoints
    if airtime_bal*1.5>okoa_limit:
        okoa_limit=int(airtime_bal*1.5)
    update_acc(number,"okoa_taken",okoa_taken)
    update_acc(number,"airtime",airtime_bal)
    update_acc(number,"okoa_limit",okoa_limit)
    update_acc(number,"bonga",bonga_bal)
    statements(number,1,initval)
    









def recharge_self(number,value):
    okoa_taken=balance_check(number,"okoa_taken")
    airtime_bal=balance_check(number,"airtime")
    okoa_limit=balance_check(number,"okoa_limit")
    bonga_bal=balance_check(number,"bonga")
    print(f"You have successfully recharged with {value}")
    bongapoints=int(value*20/100)
    initval=value
    if okoa_taken>0:
        if okoa_taken<=value:
            print(f"{okoa_taken} has been deducted to repay your okoa debt.The debt is now fully settled")
            okoa_taken=0
            value-=okoa_taken
        else:
            print(f"{value} has been deducted to to repay your okoa ebt. Dial *131# to check your remaining debt")
            okoa_taken-=value
            value=0
    airtime_bal+=value
    bonga_bal+=bongapoints
    if airtime_bal*1.5>okoa_limit:
        okoa_limit=int(airtime_bal*1.5)
    update_acc(number,"okoa_taken",okoa_taken)
    update_acc(number,"airtime",airtime_bal)
    update_acc(number,"okoa_limit",okoa_limit)
    update_acc(number,"bonga",bonga_bal)
    statements(number,1,initval)
    print(f"Your new balance is {airtime_bal}")



def scratch_recharge(number,ussd_code):
    
    if ussd_code[-1]!="#":
        print("Wrong format. every USSD must end with a '#' ")
        return
    code=ussd_code[5:10]
    value=scratch_values(code)
    
    if value==0:
       print("The voucher you have entered does not exist")
    else:recharge_self(number,value)
        

