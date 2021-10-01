import datetime
from accounts import *
from recharge import scratch_recharge,recharge
from okoa import okoa
from sms import sms
from bundles import bundles
from bonga import bonga
from mainmenu import mainmenu
from balances import balances_check
from users import *
from mpesa import mpesa
from notifications import notif_read
from sambaza import sambaza





def airtime_check(number,firstname):
    open_acc(number,firstname)
    airtime_bal=balance_search(number,firstname,"airtime_bal:")
    date = datetime.datetime.now().strftime("%d"" ""%B"" " "%Y")
    time= datetime.datetime.now().strftime("%I"":""%M"" " "%p")
    if airtime_bal==0:
        print(f"Dear customer, your balance is 0")
    else:
        print(f"Your balace on {date} at {time} was {airtime_bal}")



 


ussdkeys={
    "*100#":mainmenu,
    "*126#":bonga,
    "*131#":okoa,
    "*144#":airtime_check,
    "*544#":bundles,
    "*188#":sms,
    "*144*4#":balances_check
}

def services(number,firstname):
    notif_read(number,firstname)
    while True:
        menu=["Select an option","1.USSD","2.Mpesa","3.account"]
        for item in menu:print(item)
        choice=input(":")
        if choice=="1":
            ussd_code=input("Enter USSD Code:")
            if ussd_code[0:5]=="*141*":
                scratch_recharge(number,firstname,ussd_code)        
            elif ussd_code[0:5]=="*140*":
                sambaza(number,firstname,ussd_code)
            
            elif ussd_code in ussdkeys:
                functioncall=ussdkeys.get(ussd_code)
                function=functioncall(number,firstname)
                print("\n")
            else:
                print("Invalid USSD.Please try again")
                continue

        elif choice=="2":mpesa(number,firstname)


        elif choice=="3":
           choice=input("1.Log out\n2.Change password\n:")
           if choice=="1":return
           elif choice=="2":password_change(number)
           else: continue
        else:
            print("Invalid choice")
            continue
        continue

        
        


while True:
    print("1. Log in or\n2. create account")
    choice=input(":")
    if choice=="1":
        ret=login()
        try:
            val=ret[0]
            
        except:
            print("Wrong credentials!")
            continue
        number=ret[1]
        firstname=ret[2]
        print(f"Welcome {firstname}")
        services(number,firstname)
    elif choice=="2":
        create_acc()
        
        continue
    else:  
        print("Invalid choice")
        continue









