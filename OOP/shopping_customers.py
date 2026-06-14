import os
import json
from shopping_inventory import Products, Books, Electronics, Grocery, Stationaries, Textiles
from bank_account import BankAccount

class Customer:
    def __init__(self, user):
        self.user = user
        self.c_id = user['User ID']
        self.c_name = user['Name']
        self.c_phone = user['Phone Number']
        self.c_address = user['Address']
        self.c_balance = user['Balance']
        self.cart = []

        self.categories = {
            'books': Books(),
            'electronics': Electronics(),
            'grocery': Grocery(),
            'stationaries': Stationaries(),
            'textiles': Textiles()
        }
    ##loads data from database
    def load_data(self):
       
        file_path = "products_database.json"
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
        return {}
    
    ##retriving tax rate for each category
    def get_tax_rate(self, category):
        
        if category in self.categories:
            return self.categories[category].calc_tax()
        return 0

    def search_product(self):

        search = input("Enter product name/id to search: ").lower()
        all_products = self.load_data()

        ##list to store matched products
        matched_product = []
        ##loop through all products
        for category, product_list in all_products.items():
            for product in product_list:
                if search in product['name'].lower() or search in product['product_id'].lower():
                    matched_product.append((product, category))
        
        if matched_product:
            print("Found products:")
            for product, category in matched_product:
                print(f"  {product['name']} - {product['price']}")

        else:
            print("No products found")

        return matched_product
    ## to add items to cart
    def add_to_cart(self):
        
        p_id = input("Enter product id or name to add to cart: ")
        all_products = self.load_data()
        
        ## to find the product in the database
        for category, product_list in all_products.items():
            for product in product_list:
                if p_id == product['product_id'] or p_id == product['name']:
                    ## to get quantity and check product availability
                    try:
                        quantity = int(input("Enter quantity: "))
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                        return

                    if product['quantity'] <= 0:
                        print(f"{product['name']} is out of stock")
                        return

                    elif quantity > product['quantity']:
                        print(f"Only {product['quantity']} {product['name']} available")
                        return
                    
                    self.cart.append({
                        'product_id': product['product_id'],
                        'product_name': product['name'],
                        'product_price': product['price'],
                        'product_quantity': quantity,
                        'category': category
                    })
                    print(f"{product['name']} added to cart")
                    return
        
        print("Product not found")
    ## to remove from cart    
    def remove_from_cart(self):
        
        if not self.cart:
            print("Cart is empty")
            return
        
        self.view_cart()
        try:
            delete_id = int(input("Enter item number to remove from cart: ")) 

            if 0 <= delete_id < len(self.cart):
                removed_product = self.cart.pop(delete_id)
                print(f"{removed_product['product_name']} removed from cart")
            else:
                print("Invalid product id")

        except ValueError:
            print("Invalid input")
            return  
    
    def view_cart(self):
       
       if not self.cart:
           print("Cart is empty")
           return
       
       print("Cart:")

       total = 0
       for i, item in enumerate(self.cart, 1):
           product = item['product_name']
           price = item['product_price']
           quantity = item['product_quantity']
           category = item['category']

           
           tax_percent = self.get_tax_rate(category)
           initial_price = price * quantity
           tax_amount = initial_price * tax_percent
           item_total = initial_price + tax_amount
           total += item_total

           print(f"  Name : {product} - Price : {price} - Quantity : {quantity} - Tax Amount : {tax_amount} - Item Total : {item_total}")
       
       print(f"\nTotal Cart Amount: {total:.2f}")
           
    ## func to pay amount
    def checkout(self):
        if not self.cart:
            print("Cart is empty. Add items before checkout.")
            return
        
        total = 0
        for item in self.cart:
            price = item['product_price']
            quantity = item['product_quantity']
            category = item['category']
            tax_percent = self.get_tax_rate(category)

            total += price * quantity * (1 + tax_percent)
            
        print(f"Total Amount to pay: {total:.2f}")
        print(f"Your current bank balance is : {self.c_balance:.2f}")

        if self.c_balance < total:
            print("Insufficient balance")
            return

        ##payment logic    
        pay = input("Do you want to pay? (y/n): ")
        if pay == 'y':
            self.c_balance -= total

            # Update bank balance
            file_path = "acc_database.json"
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    users = json.load(file)
                
                for user in users:
                    if user['User ID'] == self.c_id:
                        user['Balance'] = self.c_balance
                        break
                
                with open(file_path, 'w') as file:
                    json.dump(users, file, indent=4)
            
            # Deduct inventory
            products_file = "products_database.json"
            if os.path.exists(products_file):
                with open(products_file, 'r') as file:
                    all_products = json.load(file)
                
                for item in self.cart:
                    category = item['category']
                    product_id = item['product_id']
                    quantity = item['product_quantity']
                    
                    if category in all_products:
                        for product in all_products[category]:
                            if product['product_id'] == product_id:
                                product['quantity'] -= quantity
                                break
                
                with open(products_file, 'w') as file:
                    json.dump(all_products, file, indent=4)
            
            # Reload category objects to reflect updated inventory
            for category_name in self.categories:
                self.categories[category_name].load_data()
            
            print("Payment successful")
            print(f"Your current bank balance is : {self.c_balance:.2f}")
            
            self.cart = []
        else:
            print("Payment cancelled")

    ##func to update the bank balance from this program
    def update_bank_balance(self):
        try:
            amount = float(input("Enter the amount to be added: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return
        file_path = "acc_database.json"
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                users = json.load(file)
            
            for user in users:
                if user['User ID'] == self.c_id:
                    user['Balance'] = user.get('Balance', 0) + amount
                    self.c_balance = user['Balance']
                    break
            
            with open(file_path, 'w') as file:
                json.dump(users, file, indent=4)
            
            print(f"Your current bank balance is : {self.c_balance:.2f}")
               
    def customer_menu(self):
        
        while True:
            print ("Available Options:")
            print ("1) Search Products")
            print ("2) View Cart")
            print ("3) Add to Cart")
            print ("4) Remove from Cart")
            print ("5) Checkout")
            print ("6) Update Bank Balance")
            print ("7) Exit")
            choice = input("Enter your choice (1 - 7): ")
            
            if choice == "1":
                self.search_product()
            elif choice == "2":
                self.view_cart()
            elif choice == "3":
                self.add_to_cart()
            elif choice == "4":
                self.remove_from_cart()
            elif choice == "5":
                self.checkout()
            elif choice == "6":
                self.update_bank_balance()
            elif choice == "7":
                print("Thank you for using our shopping app")
                return False
            else:
                print("Invalid choice")
                continue

##same functions to load data and login
def load_data():
        
    file_path = "acc_database.json"
        
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []
   
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

    if current_user['Role'] != 'customer':
        print("User is not a customer")
        return None

    return current_user

if __name__ == "__main__":
    
    user = login()
    if user:
        customer_obj = Customer(user)
        customer_obj.customer_menu()
