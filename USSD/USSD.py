import datetime
import os
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
from statements import state_write





def airtime_check(number):
    airtime_bal=balance_check(number,"airtime")
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

def services(number):
    notif_read(number)
    while True:
        menu=["Select an option","1.USSD","2.Mpesa","3.account"]
        for item in menu:print(item)
        choice=input(":")
        if choice=="1":
            ussd_code=input("Enter USSD Code:")
            if ussd_code[0:5]=="*141*":
                scratch_recharge(number,ussd_code)        
            elif ussd_code[0:5]=="*140*":
                sambaza(number,ussd_code)
            
            elif ussd_code in ussdkeys:
                functioncall=ussdkeys.get(ussd_code)
                function=functioncall(number)
                print("\n")
            else:
                print("Invalid USSD.Please try again")
                continue

        elif choice=="2":mpesa(number)


        elif choice=="3":
           choice=input("1.Log out\n2.Change password\n3.Statements\n:")
           if choice=="1":
               if os.path.exists("statements.txt"):
                   os.remove("statements.txt")
               return
           elif choice=="2":pass_change(number)
           elif choice=="3":
               state_write(number)
               print("Your staments have been sent to you. PLease open the Statements file to view")
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
        if ret==1:
                continue
        else:
            fname=ret[0]
            number=ret[1]
            print(f"Welcome {fname}")
            services(number)
    elif choice=="2":
        reg()
        
        continue
    else:  
        print("Invalid choice")
        continue









