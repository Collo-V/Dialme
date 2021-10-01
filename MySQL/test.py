# -*- coding: utf-8 -*-
"""
Created on Fri May  7 12:04:51 2021

@author: Collins
"""

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="FinetekAdmin2020??",
    database="ussd"
    )






mycursor=mydb.cursor()

def database():
    mycursor.execute("CREATE DATABASE ussd")

def dropdb():
     mycursor.execute("DROP DATABASE ussd")

def create_tables():
    mycursor.execute("CREATE TABLE users_regusers(user_num VARCHAR(255))")
    

def drop_tables():
    mycursor.execute("DROP TABLE user")
    
    
    
def updateTable():
    mycursor.execute("ALTER TABLE users add regdate TIMESTAMP")
    mycursor.execute("UPDATE accounts SET mpesa=1000 WHERE user_num='0713735138'")
    
    
def select():
    mycursor.execute("SELECT * FROM accounts_accounts")
    therows=mycursor.fetchall()
    print(therows)
    
def insert():
    bad="""INSERT INTO others
            VALUES  ("0799795935","Collins"),
            ("0713745138","Adenocide")"""
    
    mycursor.execute(sql)

    mydb.commit()    
    
def show():
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:print(x)
    print("\n\nTABLES\n")
    mycursor.execute("SHOW TABLES")
    for x in mycursor:print(x)


def codegenerator():
    import string,random
    pool=[str(a) for a in range(10)]+list(string.ascii_uppercase)
    p=[]
    for a in range(10):
        p.append(random.choice(pool))
    code="".join(p)
    print(code)
        
codegenerator()