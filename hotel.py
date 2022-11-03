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
    print("***7.-----Exit-----***")

    choice = int(input("Enter a choice:"))
    if(choice == 1):
        print("choice 1")
    elif(choice==2):
        print("choice 2")
    elif(choice==3):
        print("choice 3")
    elif(choice==4):
        qprint("choice 4")
    elif(choice==5):
        print("choice 5")
    elif(choice==6):
        print("choice 6")
    elif(choice==7):
        break
    
