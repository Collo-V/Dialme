from statements import statements
from notifications import notif_write
from accounts import *
from recipient import recipient

def sambaza(number,code=""):
    airtime_bal=balance_check(number,"airtime")
    if code!="":    
        if code[-1]!="#":
            print("USSD must end with a #")
            return
        code=code.split("*")
        amount=int(code[2])
        recpnum=code[-1].replace("#","")

    else:
        recpnum=input("press q to exit\nEnter the number:")
        if recpnum=="q":return
        try: amount=int(input("Enter amount:"))
        except:("Digits")
        if amount<10:
            print("minimum is 10")
            return
    if recpnum==number:
        print("You cannot sambaza to yourself")
        return
    if amount>airtime_bal:
        print("insufficient balance")
        return
    ret=recp_check(recpnum)
    if ret!=0:
        airtime_bal-=amount
        update_acc(number,"airtime",airtime_bal)
        statements(number,11,amount,recpnum)
        recipient(recpnum,amount,1,number)
        print(f"You have successfully bought kshs.{amount} worth of airtime for {recpnum}.")
    else:print("The number does not exist")
    return

