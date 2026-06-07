import random
import time
import string
from datetime import date

class bank_account:

    def __init__(self):
        self.users = []

    def register(self):
        print('Welcome to bank of new york! Kindly fill in the details to register')
        self.u_name = input("Enter Your Name:")
        self.u_id = self.u_name + "" .join(random.choices(string.ascii_letters , k=5 ))
        self.acc_no = random.randint(10000,99999)
        self.card_no = "-" .join(str(random.randint(1000,9999)) for _ in range (4))
        self.exp_date = date.today().replace(year = date.today().year + 5)
        self.ph_no = int(input("Enter your phone number : "))
        self.addr = input("Enter your address:")
        
        user_details = {
                'Name' : self.u_name,
                'User ID' : self.u_id,
                'Account Number' : self.acc_no,
                'Card No' : self.card_no,
                'Exp Date' : self.exp_date,
                'Phone Number' : self.ph_no,
                'Address' : self.addr
            }
        
        self.users.append(user_details)

        time.sleep(1)
        print(f"Congratulations! your account is registered. Your User ID is {self.u_id}")

    
    def checkaccount(self):
        
        search_id = input("Enter your User ID:")
        
        for user_details in self.users:
            if user_details['User ID'] == search_id:
                for key , value in user_details.items():
                    print(f"{key} : {value}")
                return
        
        print("User Not Found!")
            

bank = bank_account()

while True:
    choice = input("Enter your Action : 1. Register 2. Check Account 3. Exit : ")

    if choice == "1" :
        bank.register()

    elif choice == "2":
        bank.checkaccount()

    elif choice == "3":
        print("Thank you for accessing new york bank!")
        break

    else:
        print("Please Enter a valid choice")
        choice = int(input("Enter your Action : 1. Register 2. Check Account 3. Exit : "))
    




