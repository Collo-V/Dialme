from accounts import *
from statements import statements
from notifications import notif_write
from recharge import recharge


def recipient(number,amount,rtype,sendername="",sendernum=""):
    airtime_bal=balance_check(number,"airtime")
    mpesa_bal=balance_check(number,"mpesa")
    if rtype==1:
        airtime_bal+=amount
        recharge(number,amount)
        update_acc(number,"airtime",airtime_bal)
        statements(number,7,amount,sendername,sendernum)
        notif_write(number,amount,1,sendername,sendernum)


    elif rtype==2:
        mpesa_bal+=amount
        update_acc(number,"mpesa",mpesa_bal)
        statements(number,9,amount,sendername,sendernum)
        notif_write(number,amount,2,sendername,sendernum)

    else:
        mpesa_bal+=amount
        update_acc(number,"mpesa",mpesa_bal)
        statements(number,10,amount)
        notif_write(number,amount,3)



