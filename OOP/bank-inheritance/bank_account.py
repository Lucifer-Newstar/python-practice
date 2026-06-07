import random
import time
import string
from datetime import date
import os
import json


class bank_account:

    

    def __init__(self):
        
        ##to store them in a file
        self.file_path = "database.json"
        ## to restore users if exists
        self.users = self.load_data()
    
    def load_data(self):
        ##to load data if exists
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path , "r") as file:
                    return json.load(file)
                ##apparently I opened the datafile and deleted the "" of u_id and this error showed up so I came up with this and only this solution for except JSONDecodeError is from ai
            except json.JSONDecodeError:
                print("Your JSON has syntax error. i.e you messed up a comma or doublecollon or stuff that should be in JSON")
                print("The list is emptied")
                return[]
        return[]
        
    def save_data(self):
        ##to save data into folder
        with open(self.file_path , "w") as file:
            json.dump(self.users , file , indent = 4)


    def register(self):
        print('Welcome to bank of new york! Kindly fill in the details to register')
        u_name = input("Enter Your Name:")
        ##To create a id that adds random 5 letters to the user name 
        u_id = u_name + "" .join(random.choices(string.ascii_letters , k=5 ))
        acc_no = random.randint(10000,99999)
        ##To create a card number that has 16 numbers and a - between 4 numbers
        card_no = "-" .join(str(random.randint(1000,9999)) for _ in range (4))
        ##apparetly we need to make this to string to save this to JSON... sometimes using ai is better than just sitting and staring at the error for hours.
        pre_exp_date = date.today().replace(year = date.today().year + 5)
        exp_date = pre_exp_date.strftime(" %d:%m:%Y ")
        try:
            ph_no = int(input("Enter your phone number : "))
        except ValueError:
            print("Enter a valid number!")
            return
        
        addr = input("Enter your address:")
        
        user_details = {
                'Name' : u_name,
                'User ID' : u_id,
                'Account Number' : acc_no,
                'Card No' : card_no,
                'Exp Date' : exp_date,
                'Phone Number' : ph_no,
                'Address' : addr,
                'Balance' : 500
            }
        
        self.users.append(user_details)
        self.save_data()

        time.sleep(1)
        print(f"Congratulations! your account is registered. Your User ID is {u_id}")
        ## A continuity for upcomming program
        print("Amount of Rs. 500 is deposited in the account")

    
    def checkaccount(self):
        
        search_id = input("Enter your User ID:")
        
        for user_details in self.users:
            if user_details['User ID'] == search_id:
                for key , value in user_details.items():
                    print(f"{key} : {value}")
                return
        
        print("User Not Found!")

##I'm importing this to another program so I don't wanna mess up with this while loop            
if __name__ == "__main__":

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
            