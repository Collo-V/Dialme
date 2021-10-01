import datetime
import importlib
from accounts import *


def balances_check(number):
    print("\n")
    bundle_bal=balance_check(number,"bundles")
    sms_bal=balance_check(number,"sms")
    airtime_bal=balance_check(number,"airtime")
    bonga_bal=balance_check(number,"bonga")
    okoa_bal=balance_check(number,"okoa_bal")

    date = datetime.datetime.now().strftime("%d""th ""%B"" " "%Y")
    time= datetime.datetime.now().strftime("%I"":""%M"" " "%p")
    print(f"{date} {time}:\n Airtime:{airtime_bal} Bob\n {bundle_bal} Mbs Internet bundles\n {sms_bal} On net sms\n {bonga_bal} Bongapoints\n {okoa_bal} Bob Okoa balance")


