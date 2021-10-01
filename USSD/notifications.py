import datetime
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="FinetekAdmin2020??",
    database="ussd")

mycursor=mydb.cursor()

def create():
    #mycursor.execute("CREATE TABLE notifications(user_num VARCHAR(255),notif VARCHAR(500),ifread BOOLEAN)")
    #mycursor.execute("ALTER TABLE notifications MODIFY  ifread BIT ")
    pass





def notif_read(number):
    mycursor.execute(f"SELECT notif FROM notifications WHERE user_num='{number}' AND ifread=0")
    notifs=mycursor.fetchall()
    if len(notifs)>0:print(f'You have {len(notifs)} new message(s)...')
    for notif in notifs:
        print(notif[0])
    
    mycursor.execute(f"UPDATE notifications SET ifread=1 WHERE user_num='{number}'")
    mydb.commit()


    


def notif_write(number,amount,ntype,sendername="",sendernum=""):
    nkeys={
        1:f"You have received {amount} worth of airtime from {sendername}({sendernum})",
        2:f"Mpesa:You have received Kshs.{amount} from {sendername}({sendernum})",
        3:f"You deposited Kshs.{amount} at an agent",
        4:f"{amount} has been deducted to repay your okoa debt. Your debt is fully settled",
        5:f"{amount} has been deducted to repay your okoa debt. Dial *131# to check the remaining debt"
    }
    date = datetime.datetime.now().strftime("%d"" ""%B"" " "%Y")
    time= datetime.datetime.now().strftime("%I"":""%M"" " "%p")
    message=nkeys.get(ntype)
    
    
    
    notif=f'''INSERT INTO notifications
            VALUES("{number}","{date} at {time} {message}",0)'''
            
    mycursor.execute(notif)
    mydb.commit()

notif_read("0799795935")