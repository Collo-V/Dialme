import mysql.connector
from accounts import initialize


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="FinetekAdmin2020??",
    database="ussd")

mycursor=mydb.cursor()

def first():
    #mycursor.execute("CREATE DATABASE USSD") #===> Created
    #mycursor.execute("CREATE TABLE users (user_num VARCHAR(255), fname VARCHAR(255),lname VARCHAR(255), password VARCHAR(255), mpin VARCHAR(255), PRIMARY KEY(user_num))") 
    #===> CREATED
    
    #mycursor.execute("ALTER TABLE users add regdate TIMESTAMP")
    pass


def addcred(number,fname,lname,password,mpin):
        global mydb
        sql=f'''INSERT INTO users
        VALUES("{number}","{fname}","{lname}","{password}","{mpin}",NOW())'''
        
        mycursor.execute(sql)
        mydb.commit()
        return
        


def numcheck(number):
        mycursor.execute("SELECT user_num FROM users")
        numbers=mycursor.fetchall()
        for num in numbers:
           if number in num:return 1
           else:return 0
              
        
        


def reg():
    global mycursor
    while True:
      number=input("press q to cancel\nEnter your number:")
      if number=="q":return
      try:
          number=int(number)
      except:
          print("Number must be digits")
          continue
      number="0"+str(number)
      if len(number)!=10:
          print("The digits must be 10")
          continue
      ret=numcheck(number)
      if ret==1:
          print("The number is already registered")
          continue
    
      fname=input("Enter your First Name:")  
      lname=input("Enter the your Last Name:")
           
      print(f"number:{number}\n first name:{fname}\nLast Name:{lname}")
      choice=input("press 1 to edit, any other key to proceed:")
      if choice=="1": continue
      else:break
    while True:
        password=input("Enter the password:")
        if len(password)<5:
            print("Password must be at least 5 characters long")
            continue
        if password!=input("Re-enter password:"):
            print("Passwords do not match!")
            continue
        else:break
    while True:
        mpin=input("Set mpesa pin:")
        if mpin!=input("re-enter Pin:"):
                print("PINs do not match")
                continue
        else: break
    addcred(number, fname, lname, password, mpin)
    initialize(number)
    print("Account created successfully")
    return
    


def login():
    number=input("enter your number:")
    try:
        mycursor.execute(f"SELECT password FROM users WHERE user_num='{number}'")
        if mycursor.fetchone()[0]!=input("Enter Password:"):
            print("Wrong credentials!")
            return 1
        else:
            mycursor.execute(f"SELECT fname FROM users WHERE user_num='{number}'")
            return mycursor.fetchall()[0][0],number
    
    except:
        print("The number is not registered")
        return 1


def pass_change(number):
    mycursor.execute(f"SELECT password FROM users WHERE user_num='{number}'")
    password=mycursor.fetchone()[0]
    if password!=input("Enter the old password:"):
        print("Wrong password")
        return
    newpass=input("Enter new password:")
    if newpass!=input("Re-enter new Password:"):
        print("Passwords do not match")        
        return
    mycursor.execute(f"UPDATE users SET password='{newpass}' WHERE user_num='{number}'")
    mydb.commit()   



        

    
    


    
    
    
    
            