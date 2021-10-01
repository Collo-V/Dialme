import datetime
from okoa import okoa
from sms import sms
from bundles import bundles
from bonga import bonga
from balances import balances_check
from accounts import *
from sambaza import sambaza



def mainmenu(number,firstname):
    print("\n")
    menu=["Please select a service","1.Top up","2.Bundles","3.Sms bundles","4.bonga","5. Okoa","6.Check balances","7.Sambaza","Press any key to exit"]
    for item in menu:
        print (item)
    choice=input(":")
    if choice=="1":print("Please dial *141*SractchcardPin#")
    elif choice=="2":bundles(number)
    elif choice=="3":sms(number)
    elif choice=="4":bonga(number)
    elif choice=="5":okoa(number)
    elif choice=="6":balances_check(number)
    elif choice=="7":sambaza(number)
    else:return

