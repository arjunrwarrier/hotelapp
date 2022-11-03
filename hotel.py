import mysql.connector
import sys
from datetime import datetime

try:
    mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'hoteldb')
except mysql.connector.Error as e:
    sys.exit("Connection Error")
mycursor = mydb.cursor()

#creating a menudriven
items=[]
total = 0
while(True):
    print("***Wellcome to SnackHotel***")
    print("###Select your items###")
    print("***1.Tea-------10rs***")
    print("***2.Coffee----20rs***")
    print("***3.Vada------15rs***")
    print("***4.Sandwich--30rs***")
    print("***5.Burger----40rs***")
    print("***6.-----Bill-----***")
    print("***7.View all transaction**")
    print("***8.View transaction summary**")
    print("***9.View transaction summary of a period.**")
    print("***10.-----Exit-----***")

    choice = int(input("Enter a choice:"))
    if(choice == 1):
        quantity=int(input("Please enter the quantity: "))
        total += 10*quantity
        items.append("Tea x "+str(quantity))
    elif(choice==2):
        quantity=int(input("Please enter the quantity: "))
        total += 20*quantity
        items.append("Coffee x "+str(quantity))
    elif(choice==3):
        quantity=int(input("Please enter the quantity: "))
        total += 15*quantity
        items.append("Vada x "+str(quantity))
    elif(choice==4):
        quantity=int(input("Please enter the quantity: "))
        total += 30*quantity
        items.append("Sandwich x "+str(quantity))
    elif(choice==5):
        quantity=int(input("Please enter the quantity: "))
        total += 40*quantity
        items.append("Burger x "+str(quantity))
    elif(choice==6):
        name = input("Enter your name: ")
        phone = input("Enter your phone: ")
        print("######Your Bill#####")
        print("Name: ",name)
        print("Phone: ",phone)
        date = datetime.today().strftime('%Y-%m-%d')
        print("Date : "+date)
        print("***Purchased Items***")
        for i in items:
            print(i)
        print("Total bill = ",total)
        try:
            sql = "INSERT INTO `bills`(`name`, `phone`, `amount`, `date`) VALUES (%s,%s,%s,now())"
            data=(name,phone,total)
            mycursor.execute(sql,data)
            mydb.commit()
        except mysql.connector.Error as e:
            sys.exit(e)
        print("Data inserted into database")
        items=[]
        total = 0
    elif(choice ==7):
        print("View All transaction date wise")
        dbill = input("Enter the date: ")
        try:
            sql = "SELECT `name`, `phone`, `amount`, `date` FROM `bills` WHERE `date`= '"+dbill+"'"
            mycursor.execute(sql)
            result = mycursor.fetchall()
        except mysql.connector.Error as e:
            sys.exit("connector error")
        for i in result:
            print("name: ",i[0])
            print("phone: ",i[1])
            print("amount: ",i[2])
            print("date: ",i[3],"\n")
    elif(choice ==8):
        print("View the transaction summary")
        dbill = input("Enter the date: ")
        try:
            sql = "SELECT  SUM(`amount`) FROM `bills` WHERE `date` = '"+dbill+"'"
            mycursor.execute(sql)
            result = mycursor.fetchall()
        except mysql.connector.Error as e:
            sys.exit("Connection error")
        for i in result:
            r = str(i[0])
        print(f"The total Amount recieved in {dbill} :  ",r)
    elif(choice ==9):
        print("View the transaction summary of a period")
        dbill = input("Enter the first date: ")
        dbill2=input("Enter the second date: ")
        try:
            sql = "SELECT SUM(`amount`) FROM `bills` WHERE `date` BETWEEN '"+dbill+"' AND '"+dbill2+"'"
            mycursor.execute(sql)
            result = mycursor.fetchall()
        except mysql.connector.Error as e:
            sys.exit(e)
        for i in result:
            r = str(i[0])
        print(f"The total Amount recieved from {dbill} and {dbill2} :  ",r)
            

    elif(choice==10):
        break
    
