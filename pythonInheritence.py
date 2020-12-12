import random
import sys

i = 0

class hotel:
    
    
    def __init__(self):
        
        self.name = []
        self.phone = []
        self.address = []
        self.days = []
        self.room = []
        self.price  = []
        self.room_number = []
        self.customer_id = []
        
    def booking(self):
    
        global i
        print("\t\tRoom Booking")
        print("\t-------------------")
        n = str(input("\tEnter Name\t"))
        ph = str(input("\tEnter phone number\t"))
        a = str(input("\tEnter address\t"))
        d = int(input("\tEnter number of days\t"))
        self.name.append(n)
        self.phone.append(ph)
        self.address.append(a)
        self.days.append(d)
        
        print("\nSelect Room Type")
        print("\n 1. standard non AC - Rs. 3000")
        print("\n 2. standard AC - Rs. 3500")
        print("\n 3. 3-Bed non AC - Rs. 4000")
        print("\n 4. 3-Bed AC - Rs. 4500")
        ch = int(input("Enter your choice\t"))
            
        if ch == 1:
            self.room.append('standard non AC')
            print("\n room type - standard non AC")
            self.price.append(3000)
            print("\n price : Rs. 3000")
        elif ch == 2:
            self.room.append('standard AC')
            print("\n room type - standard non AC")
            self.price.append(3500)
            print("\n price : Rs. 3500")
        elif ch == 3:
            self.room.append('3 - Bed non AC')
            print("\n room type - standard non AC")
            self.price.append(4000)
            print("\n price : Rs. 4000")
        elif ch == 4:
            self.room.append('3-Bed AC')
            print("\n room type - standard non AC")
            self.price.append(4500)
            print("\n price : Rs. 4500")
        else:
            print("wrong Entry")
        room_n = random.randrange(99)+100
        cust_id = random.randrange(99)+1000
        while room_n in self.room or cust_id in self.customer_id:
            room_n = random.randrange(99)+100
            cust_id = random.randrange(99)+1000
        print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")
        print("Room No. - ", room_n)
        print("Customer Id - ", cust_id)
        self.room_number.append(room_n)
        self.customer_id.append(cust_id)
        i = i+1
        n = int(input("0-BACK\n ->"))
        if n == 0:
            self.home()
        else:
            exit()
            
    def payment(self):

        ph = str(input("Phone Number: "))
        global i
        f = 0
    
        for n in range(0, i):
            if ph == self.phone[n]:
    
                f = 1
                print(" Payment")
                print(" --------------------------------")
                print("\n  Amount: ", (self.price[n]*self.days[n]))
                print("\n         confirm payment")
                print("  (y/n)")
                ch = str(input("->"))
                if ch == 'y' or ch == 'Y':
                    print("\n\n --------------------------------")
                    print("           Hotel AnCasa")
                    print(" --------------------------------")
                    print("              Bill")
                    print(" --------------------------------")
                    print(" Name: ", self.name[n], "\t\n Phone No.: ", self.phone[n])
                    print("\t\n Address: ", self.address[n], "\t")
                    print("\n Room Type: ", self.room[n])
                    print("\t\n Room Charges: ", self.price[n]*self.days[n], "\t")
                    print(" --------------------------------")
                    print("\n Total Amount: ", self.price[n]*self.days[n], "\t")
                    print(" --------------------------------")
                    print("          Thank You")
                    print("          Visit Again :)")
                    print(" --------------------------------\n")
                    self.room_number.pop(n)
                    self.customer_id.pop(n)
                    self.room_number.insert(n, 0)
                    self.customer_id.insert(n, 0)
            else:
                    print("\ninvalid phone number\t")
                    self.payment()
        if f == 0:
            print("Invalid Customer Id")
    
        n = int(input("0-BACK\n ->"))
        if n == 0:
            self.home()
        else:
            exit()
            
class details:
    
    
    def rooms_info(self):
        print("\n\t\tRoom Details")
        print("\n\t\t--------------------")
        print("\n\t\t 1. Standard Non AC")
        print("\n\t\t 2. Standard  AC")
        print("\n\t\t 3. 3 - Bed Non AC")
        print("\n\t\t 4. 3 - Bed AC")
        ch = int(input("Enter choice\t"));
        
        if ch == 1:
                print("\n\t\tSTANDARD NON-AC") 
                print("\t-----------------------------------------------") 
                print("\n\t\tRoom amenities include: 1 Double Bed, Television, Telephone,") 
                print("\n\t\tDouble-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and") 
                print("\n\t\tan attached washroom with hot/cold water.\n")
        elif ch == 2:
            print("\n\t\tSTANDARD NON-AC") 
            print("\n\t--------------------------------------------------") 
            print("Room amenities include: 1 Double Bed, Television, Telephone,") 
            print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and") 
            print("an attached washroom with hot/cold water + Window/Split AC.\n") 
        elif ch == 3:
            print("\n\t\t3-Bed NON-AC") 
            print("\n\t----------------------------------------------------") 
            print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,") 
            print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1") 
            print("Side table, Balcony with an Accent table with 2 Chair and an") 
            print("attached washroom with hot/cold water.\n")
        elif ch == 4:
            print("\n\t\t3-Bed AC") 
            print("\n\t------------------------------------------------------") 
            print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,") 
            print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ") 
            print("1 Side table, Balcony with an Accent table with 2 Chair and an") 
            print("attached washroom with hot/cold water + Window/Split AC.\n\n")
        else:
            print("\n\t invalid entry")
            
        ch = int(input("\n\t 0 - Back 1- Main Menu\t"))
        if ch == 0:
            self.rooms_info()
        
        
        
class menu(hotel, details):
    
    def home(self):

        print("\t\t\t\tWELCOME")
        print("-------------------------------------------")
        print("\n\t\t\t 1. Booking ")
        print("\n\t\t\t 2. Payment")
        print("\n\t\t\t 3. Rooms_info")
        print("\n\t\t\t 4. Exit")
        ch = int(input("Enter Choice\t"))
        if ch == 1:
            self.booking()
        elif ch == 2:
            self.payment()
        elif ch == 3:
            self.rooms_info()
        else:
            sys.exit(0)
    
    
        
    

a = menu()        
while 1:
    a.home()


   
    
    
  
    