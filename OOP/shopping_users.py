import sys
import os
import json
from bank_account import bank_account

class users:
    def __init__(self):
        self.users = []
        self.file_path = "acc_database.json"
        self.load_data()
        
    def load_data(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as file:
                    data = json.load(file)
                    for user in data:
                        self.users.append(user)
            except json.JSONDecodeError:
                print("Your JSON has syntax error. i.e you messed up a comma or doublecollon or stuff that should be in JSON")
                sys.exit()
        else:
            print("No data found")
            self.users = []
        
        return self.users
    
    def save_data(self):
        with open(self.file_path, "w") as file:
            json.dump(self.users, file, indent=4)

    def register(self):
        u_id = input("Enter your user ID: ")
        users = self.load_data()
        
        user_found = None
        for user in users:
            if user["User ID"] == u_id:
                user_found = user
                break

        if not user_found:
            print("User not found")
            print("Please register at the bank first.")
            return
        
        if 'Role' in user_found:
            print(f"You are already registered as a {user_found['Role']}")
            return
        
        print(f"Welcome {user_found['Name']}")
        choice = input("Choose your role (customer/seller): ")
    
        if choice == "customer" or choice == "1":
            role = "customer"
        elif choice == "seller" or choice == "2":
            role = "seller"
        else:
            print("Invalid choice")
            return
        
        user_found['Role'] = role

        self.save_data()

        print(f"You are registered as {role}")
        

if __name__ == "__main__":
    reg = users()
    reg.register()