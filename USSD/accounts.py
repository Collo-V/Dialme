# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:53:03 2021

@author: Collins
"""

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="FinetekAdmin2020??",
    database="ussd")

mycursor=mydb.cursor()

def create():
        pass
        #mycursor.execute("CREATE TABLE accounts(user_num VARCHAR(255),airtime FLOAT(5,2),bundles FLOAT(5,2),bonga FLOAT(5,2),sms FLOAT(5,2),okoa_limit FLOAT(5,2),okoa_taken FLOAT(5,2),okoa_bal FLOAT(5,2),mpesa FLOAT(6,2))")
        #mycursor.execute("ALTER TABLE accounts ADD PRIMARY KEY(user_num)")
        
#create()

def initialize(number):
    sql=f'''INSERT INTO accounts
        VALUES("{number}",0,0,0,0,0,0,0,0)'''
    mycursor.execute(sql)
    mydb.commit()





def update_acc(number,account,value):
    mycursor.execute(f"UPDATE accounts SET {account}={value} WHERE user_num='{number}'")
    mydb.commit()
    

    


def balance_check(number,account):
        mycursor.execute(f"SELECT {account} from accounts WHERE user_num='{number}'")
        return mycursor.fetchall()[0][0]

def recp_check(number):
    mycursor.execute(f"SELECT fname FROM users WHERE user_num='{number}'")
    fname=mycursor.fetchall()
    if fname==[]:return 0
    else: return fname[0][0]

def pin_check(number):
    mycursor.execute(f"SELECT mpin from users WHERE user_num='{number}'")
    pin=mycursor.fetchall()[0][0]
    return pin
