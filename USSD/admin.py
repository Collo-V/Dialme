from accounts import*
from mpesa import recp_check
from recipient import recipient



menukeys={
    "okoa bal":"okoa_bal:",
    "okoa taken":"okoa_taken:",
    "airtime balance":"airtime_bal:",
    "bonga balance":"bonga_bal:",
    "bundle balance":"bundle_bal:",
    "sms balance":"sms_bal:"
}
def update(number,firstname):

    while True:
        menu=["okoa bal","okoa taken","airtime balance","bonga balance","bundle balance","sms balance"]
        print("What do you want to change?")
        for n in range(len(menu)):
            print(f"{n}.{menu[n]}")
        choice=int(input(":")) 
        while True:
            
            try:
                value=int(input(f"update {menu[choice]} to what:(press any keyto go back)"))
                if value<0:
                    print("value can never be negative")
                    continue
                else:break
            except:
                break
        break
    update_acc(number,firstname,menukeys.get(menu[choice]),value)
    print(f"{menu[choice]} updated successfully!")


def deposit(number,firstname):
    while True:
        try:
           amount=int(input("Enter amount:"))
           if amount<20:
            print("Minimum is 20")
            continue
           else:break
        
        except:
            print("Digits please")
            continue
    print(f"Confirm deposit of {amount} to {firstname} ({number})")
    if input("press 00 to deny, any other key to accept:")!="00":
       
        recipient(number,firstname,amount,3)

        

while True:
    ret=recp_check(input("Enter number:"))
    try:
        recpnum=ret[1]
        recpname=ret[0]
        break
    except:
        print("The number does not exist")
        continue
print("1.balances\n2.Mpesa deposit")
choice=input(":")
if choice=="1":update(recpnum,recpname)
elif choice=="2":deposit(recpnum,recpname)
