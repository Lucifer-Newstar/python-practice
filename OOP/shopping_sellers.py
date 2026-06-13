import os
import sys
import json
from bank_account import bank_account
from shopping_inventory import items ,books, electronics, grocery, stationaries, textiles

class seller:
    def __init__(self, seller_id , name , email , phone , address):
        self.s_id = seller_id
        self.s_name = name
        self.s_email = email
        self.s_phone = phone
        self.s_address = address
        self.s_bank_account = bank_account()

        self.electronics = electronics()
        self.stationaries = stationaries()
        self.textiles = textiles()
        self.books = books()
        self.grocery = grocery()

        self.categories = {
            "electronics" : self.electronics ,
            "stationaries" : self.stationaries ,
            "textiles" : self.textiles ,
            "books" : self.books ,
            "grocery" : self.grocery
        }

    def add_item(self):
        
        print("Available categories: electronics, stationaries, textiles, books, grocery")
        category = input("Enter product type: ").lower()

        if category not in self.categories:
            print("Invalid Product Category")
            return
        
        try:
            p_id = int(input("Enter product ID: "))
            p_name = input("Enter product name: ")
            p_price = float(input("Enter product price: "))
            p_quantity = int(input("Enter product quantity: "))
            
            new_product = products(p_id, p_name, p_price, category)
            self.categories[category].add_product(new_product)

            self.categories[category].add_product(new_product)

            tax_rate = self.categories[category].calc_tax()
            print(f"Tax rate for {category}: {tax_rate * 100}%")

        except ValueError:
            print("Invalid input. Please enter valid values.")
            return


    def remove_item(self):
        category = input(print("Enter product type: ")).lower()

        if category not in self.categories:
            print("Invalid Product Category")
            return
        
        p_id = int(input("Enter product ID: "))
        self.categories[category].remove_product(p_id)
    
    def display(self):
        print(f"Hello {self.s_name}. your inventory list is:")
        for category in self.categories.values():
            category.display_products()

if __name__ == "__main__":
    
    pass


