import random
import sys

name = []
phone = []
address = []
days = []
room = []
price = []
room_number = []
customer_id = []

i = 0


def home():

    print("\t\t\t\tWELCOME")
    print("-------------------------------------------")
    print("\n\t\t\t 1. Booking ")
    print("\n\t\t\t 2. Payment")
    print("\n\t\t\t 3. Exit")
    ch = int(input("Enter Choice\t"))
    if ch == 1:
        booking()
    elif ch == 2:
        payment()
    else:
        sys.exit(0)


def booking():
    global i
    print("\t\tRoom Booking")
    print("\t-------------------")
    n = str(input("\tEnter Name\t"))
    ph = str(input("\tEnter phone number\t"))
    a = str(input("\tEnter address\t"))
    d = int(input("\tEnter number of days\t"))
    name.append(n)
    phone.append(ph)
    address.append(a)
    days.append(d)
    print("\nSelect Room Type")
    print("\n 1. standard non AC - Rs. 3000")
    print("\n 2. standard AC - Rs. 3500")
    print("\n 3. 3-Bed non AC - Rs. 4000")
    print("\n 4. 3-Bed AC - Rs. 4500")
    print("\n 0. show room prices")
    ch = int(input("Enter your choice\t"))
    if ch == 1:
        room.append('standard non AC')
        print("\n room type - standard non AC")
        price.append(3000)
        print("\n price : Rs. 3000")
    elif ch == 2:
        room.append('standard AC')
        print("\n room type - standard non AC")
        price.append(3500)
        print("\n price : Rs. 3500")
    elif ch == 3:
        room.append('3 - Bed non AC')
        print("\n room type - standard non AC")
        price.append(4000)
        print("\n price : Rs. 4000")
    elif ch == 4:
        room.append('3-Bed AC')
        print("\n room type - standard non AC")
        price.append(4500)
        print("\n price : Rs. 4500")
    else:
        print("wrong Entry")
    room_n = random.randrange(99)+100
    cust_id = random.randrange(99)+1000
    while room_n in room or cust_id in customer_id:
        room_n = random.randrange(99)+100
        cust_id = random.randrange(99)+1000
    print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")
    print("Room No. - ", room_n)
    print("Customer Id - ", cust_id)
    room_number.append(room_n)
    customer_id.append(cust_id)
    i = i+1
    n = int(input("0-BACK\n ->"))
    if n == 0:
        home()
    else:
        exit()


def payment():

    ph = str(input("Phone Number: "))
    global i
    f = 0

    for n in range(0, i):
        if ph == phone[n]:

            f = 1
            print(" Payment")
            print(" --------------------------------")
            print("\n  Amount: ", (price[n]*days[n]))
            print("\n         confirm payment")
            print("  (y/n)")
            ch = str(input("->"))
            if ch == 'y' or ch == 'Y':
                print("\n\n --------------------------------")
                print("           Hotel AnCasa")
                print(" --------------------------------")
                print("              Bill")
                print(" --------------------------------")
                print(" Name: ", name[n], "\t\n Phone No.: ", phone[n])
                print("\t\n Address: ", address[n], "\t")
                print("\n Room Type: ", room[n])
                print("\t\n Room Charges: ", price[n]*days[n], "\t")
                print(" --------------------------------")
                print("\n Total Amount: ", price[n]*days[n], "\t")
                print(" --------------------------------")
                print("          Thank You")
                print("          Visit Again :)")
                print(" --------------------------------\n")
                room_number.pop(n)
                customer_id.pop(n)
                room_number.insert(n, 0)
                customer_id.insert(n, 0)
        else:
                print("\ninvalid phone number\t")
                payment()
    if f == 0:
        print("Invalid Customer Id")

    n = int(input("0-BACK\n ->"))
    if n == 0:
        home()
    else:
        exit()
home()
