import os
import sys
import json
from shopping_inventory import Products, Items, Books, Electronics, Grocery, Stationaries, Textiles
from bank_account import BankAccount

class Seller:
    def __init__(self, user_data):
        ## to initialize seller data
        self.user_data = user_data
        self.s_id = user_data['User ID']
        self.s_name = user_data['Name']
        self.s_phone = user_data['Phone Number']
        self.s_address = user_data['Address']
        self.s_balance = user_data['Balance']

        ## to initialize categories

        self.electronics = Electronics()
        self.stationaries = Stationaries()
        self.textiles = Textiles()
        self.books = Books()
        self.grocery = Grocery()

        self.categories = {
            "electronics" : self.electronics ,
            "stationaries" : self.stationaries ,
            "textiles" : self.textiles ,
            "books" : self.books ,
            "grocery" : self.grocery
        }

    def add_item(self):
        ## to add item to inventory

        print("Available categories: electronics, stationaries, textiles, books, grocery")
        category = input("Enter product type: ").lower()

        ## if seller decides to enter a non-existent category even after printing available categories
        if category not in self.categories:
            print("Invalid Product Category. We can't add new one just for you sorry!")
            return
        ## to add products
        try:
            p_id = input("Enter product ID: ")
            p_name = input("Enter product name: ")
            p_price = float(input("Enter product price: "))
            p_quantity = int(input("Enter product quantity: "))
            
            if p_price <= 0:
                print("Price must be greater than 0.")
                return
            if p_quantity <= 0:
                print("Quantity must be greater than 0.")
                return
            
            new_product = Products(p_id, p_name, p_price, category)
            new_product.quantity = p_quantity
            self.categories[category].add_product(new_product)
            self.categories[category].save_data()

            tax_rate = self.categories[category].calc_tax()
            print(f"Tax rate for {category}: {tax_rate * 100}%")

        except ValueError:
            print("Invalid input. Please enter valid values.")
            return

    ## to remove products
    def remove_item(self):
        category = input("Enter product type: ").lower()

        if category not in self.categories:
            print("Invalid Product Category")
            return
        
        p_id = input("Enter product ID: ")

        # Check if product exists before removing
        product_exists = False
        for product in self.categories[category].products:
            if product.product_id == p_id:
                product_exists = True
                break
        
        if not product_exists:
            print(f"Product ID {p_id} not found in {category}")
            return

        delete = Products(p_id, "", 0, category)
        self.categories[category].remove_product(delete)
    
    def display(self):
        print(f"Hello {self.s_name}. your inventory list is:")
        has_products = False

        for c_name, c_object in self.categories.items():
            
            if c_object.products:
                has_products = True
                c_object.display_products()
                print(f"Total products in {c_name}: {len(c_object.products)}")
        
        if not has_products:
            print("Not yet! add products in inventory to look into em")
        
    def seller_menu(self):
        while True:
            print("\n1. Add Product")
            print("2. Remove Product")
            print("3. Display Products")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_item()
            elif choice == '2':
                self.remove_item()
            elif choice == '3':
                self.display()
            elif choice == '4':
                break
            else:
                print("Invalid choice")
## to load existing data
def load_data():
        
    file_path = "acc_database.json"
        
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []
##login logic    
def login():
    user_id = input("Enter user ID: ")
    user_data = load_data()

    current_user = None

    for user in user_data:
        if user['User ID'] == user_id:
            current_user = user
            break
            
    if not current_user:
        print("User not found")
        choice = input("Do you want to register to New York Bank? (y/n): ").lower()
        if choice == 'y':
            return None
        else:
            bank = BankAccount()
            bank.register()

            print("Registration successful. Login with your new ID!")
            return None

    if current_user['Role'] != 'seller':
        print("User is not a seller")
        return None

    return current_user
    

if __name__ == "__main__":
    
    user = login()
    if user:
        seller_obj = Seller(user)
        seller_obj.seller_menu()