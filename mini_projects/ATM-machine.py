from bank_account import BankAccount
import time
import os
import json

class BankBalance:

    def __init__(self):
        self.current_balance = 0

class ATM(BankBalance):

    def __init__(self, bank_instance):
        ## to initialize BankBalance class
        super().__init__()
        self.bank = bank_instance
        self.user = None

    def login(self):
        print("Welcome to bank of new york!")
        atm_u_id = input("Enter your User ID: ")
        ## to load data from json file
        self.bank.users = self.bank.load_data()

        for user in self.bank.users:
            if user["User ID"] == atm_u_id:
                self.user = user
                self.current_balance = user["Balance"]
                print(f"Welcome {user['Name']} !")
                return True
            
        print("User ID not found! Register your account if you're new")
        return False
    ##function to deposit money
    def deposit(self):
        
        try:
            self.deposit_amt = int(input("Enter the deposit amount:"))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

        if self.deposit_amt <= 0:
            print("The amount deposited can't be 0 or Low")
            return
        
        self.current_balance += self.deposit_amt
        

        self.user["Balance"] = self.current_balance
        self.bank.save_data()

        time.sleep(1)
        print(f"Amount Rs. {self.deposit_amt} is deposited to your account")

    ##function to withdraw money
    def withdraw(self):

        try:
            self.withdraw_amt = int(input("Enter the withdrawal amount:"))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

        if self.withdraw_amt > self.current_balance:
            print("Insufficient Bank Balance! You're Broke!")
            return
        
        elif self.withdraw_amt <= 0:
            print("The amount to be withdrawn can't be 0 or Low")
            return
        ##to reduce the amount from current balance
        self.current_balance -= self.withdraw_amt

        self.user["Balance"] = self.current_balance
        self.bank.save_data()

        time.sleep(1)
        print(f"Amount Rs. {self.withdraw_amt} is withdrawn from your account")
    
    def check_balance(self):

        print(f"Your account balance is : {self.current_balance}")

if __name__ == "__main__":
    ##to create an instance of bank_account 
    bank = BankAccount()
    ##to create an instance of ATM class
    atm = ATM(bank)
    ##atm user login
    if atm.login():
        while True:
            print(f"Welcome to New York Bank ATM , {atm.user['Name']}.")
            print("\n=== ATM MACHINE MENU ===")
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Check Balance")
            print("4. Exit")
            
            choice = input("Select your Action (1-4): ")
            
            if choice == "1":
                atm.deposit()
            elif choice == "2":
                atm.withdraw()
            elif choice == "3":
                atm.check_balance()
            elif choice == "4":
                print("Thank you for using Bank of New York ATM. Goodbye!")
                break
            else:
                print("Invalid selection. Please try again.")