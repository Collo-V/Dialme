from statements import statements
import datetime
from accounts import *
from recipient import recipient
from recharge import recharge,recharge_self




def buy_airtime(number,mpesa_bal,):
    choice=input("1. My number\n2.Other number\n:")
    if choice=="1":
        recpname="(self)"
        recpnum=number

    elif choice=="2":
        num=input("Enter the other number:")
        if num==number:
            print("You cannot buy for yourself pick 'buy for my number' option")
            return            
        recpname=recp_check(num)
        recpnum=num
        if recpname==0:
            print("The number does not exist")
            return
    else:
        print("Invalid choice")
        return
    while True:
        try:
            amount=int(input("Enter amount:"))
            break
        except:
            print("Digits Please!!")
            continue
    if amount<5:
        print("minimum is 5")
        return
    print(f"Buy airtime of {amount} for {recpnum} {recpname}?")
    pin=pin_check(number)
    if pin!=input("Enter mpesa PIN:"):
        print("You have entered the wrong pin")
    else:
        if mpesa_bal<amount:
            print("insufficient balance")
            return
        mpesa_bal-=amount
        if recpname=="(self)":
            print(f"You have successfully bought kshs.{amount} worth of airtime. Mpesa balance:{mpesa_bal}")
            recharge_self(number,amount)
            update_acc(number,"mpesa_bal:",mpesa_bal)
            statements(number,6,amount)
            
            

        else:
            recipient(recpnum,amount,1,number,)
            statements(number,12,amount,recpnum)
            print(f"You have successfully bought kshs.{amount} worth of airtime for {recpnum}. Mpesa balance:{mpesa_bal}")

def mpesa(number):
    while True:
        mpesa_bal=balance_check(number,"mpesa")
        print("press q to exit\n1.Buy airtime\n2.Send money\n3.Check balance")
        choice=input(":")
        if choice=="q":return
        elif choice=="1":
            buy_airtime(number,mpesa_bal,)
            continue
        elif choice=="2":
            num=input("Enter the other number:")
            recpname=recp_check(num)
            if recpname==0:
                print("The number does not exist")
                continue
            if num==number:
                print("You cannot send money to yourself")
                continue
            recpnum=num
            while True:
                try:
                    amount=int(input("Enter amount:"))
                    break
                except:
                    print("Digits Please!!")
                    continue
            if amount<5:
                print("minimum is 5")
                return
            print(f"Send kshs.{amount} to {recpname}({recpnum}) ?")
            pin=pin_check(number)
            if pin!=input("Enter mpesa PIN:"):
                print("You have entered the wrong pin")
            else:
                if mpesa_bal<amount:
                    print("insufficient balance")
                    return
                mpesa_bal-=amount
                update_acc(number,"mpesa",mpesa_bal)
                statements(number,8,amount,recpname,recpnum)
                recipient(recpnum,amount,2,number,)
                print(f"You have successfully sent kshs.{amount} to {recpname} ({recpnum}). Mpesa balance:{mpesa_bal}")
        elif choice=="3":
            date = datetime.datetime.now().strftime("%d"" ""%B"" " "%Y")
            time= datetime.datetime.now().strftime("%I"":""%M"" " "%p")
            print(f"{date} {time}:\nyour mpesa balance was {mpesa_bal}")  
        else:
            print("Invalid choice")          
            continue

        return


               