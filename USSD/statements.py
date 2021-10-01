import datetime
from accounts import *
import datetime
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="FinetekAdmin2020??",
    database="ussd")

mycursor=mydb.cursor()

def create():
    #mycursor.execute("CREATE TABLE statements(user_num VARCHAR(255),statements VARCHAR(500),sdate TIMESTAMP)")
    pass





def state_write(number):
    mycursor.execute(f"SELECT fname,lname FROM users WHERE user_num='{number}'")
    details=mycursor.fetchall()
    fname=details[0][0]
    lname=details[0][1]
    mycursor.execute(f"SELECT statements FROM statements WHERE user_num='{number}' ORDER BY sdate DESC")
    statements=mycursor.fetchall()
    with open("statements.txt","w") as state:
        state.write(f"STATEMENT FOR {fname} {lname}:\n")
        for statement in statements:
                state.write(f"{statement[0]}\n\n")
    
    return

def statements(number,stype,value=0,spend=0,rtype=0):
    airtime_bal=balance_check(number,"airtime")
    bonga_bal=balance_check(number,"bonga")
    mpesa_bal=balance_check(number,"mpesa")

    statekeys={
    0:"Created account",
    1:f"Recharged with {value},balace:{airtime_bal}",
    2:f"Bought {value} Mbs for {spend},balace:{airtime_bal}",
    3:f"Bought {value} Sms for {spend},balace:{airtime_bal}",
    4:f"Redeemed {value} bongapoints for {spend} {rtype}, bonga balnce:{bonga_bal}",
    5:f"Took {value} worth of okoa",
    6:f" bought {value} worth of airtime, Mpesa balance:{mpesa_bal}",

    7:f"received {value} worth of airtime from {spend}({rtype}),airtime balace:{airtime_bal}",
    8:f"Sent {value} Kshs to  {spend}({rtype}), Mpesa balance:{mpesa_bal}",
    9:f"Received {value} Kshs from {spend}({rtype}), Mpesa balance:{mpesa_bal}",
    10:f"deposited Kshs.{value}. Mpesa balance:{mpesa_bal}",
    11:f"Transfered {value} worth of airtime to {spend}",
    12:f" bought {value} worth of airtime for {spend}, Mpesa balance:{mpesa_bal}",

    }

    date = datetime.datetime.now().strftime("%d"" ""%B"" " "%Y")
    time= datetime.datetime.now().strftime("%I"":""%M"" " "%p")
    statement=statekeys.get(stype)
    
    sql=f"""INSERT INTO statements 
    VALUES('{number}','{date} at {time}... \n {statement}',NOW())"""
    mycursor.execute(sql)
    mydb.commit()
    
