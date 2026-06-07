from bank_account import bank_account
import time

class bank_balance(self):
    
    self.current_balance = 0

class ATM:

    b = bank_balance
    
    def deposit():
        
        deposit_amt = int(input("Enter the deposit amount:"))
        b.current_balance += deposit_amt
        time.sleep(1)
        print(f"Amount Rs. {deposit_amt} is deposited to your account")

    def withdraw():

        withdraw_amt = int(input("Enter the withdrawal amount:"))
        b.current_balance -= deposit_amt
        time.sleep(1)
        print(f"Amount Rs. {withdraw_amt} is withdrawn from your account")