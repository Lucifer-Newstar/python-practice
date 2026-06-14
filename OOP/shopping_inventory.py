import os
import json
import sys
from abc import ABC, abstractmethod

class Products:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.quantity = 0
    ## to represent the object as string
    def __str__(self):
        return f"{self.name} - ${self.price} (ID: {self.product_id})"

    ## to convert objects as dictionaries 
    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "quantity": self.quantity
        }
    
    ## static method used for converting dictionary to object
    @staticmethod
    def from_dict(data):
        product = Products(data["product_id"], data["name"], data["price"], data["category"])
        product.quantity = data["quantity"]
        return product
    
class Items(ABC):
    
    def __init__(self, category):
        self.category = category
        self.products = []
        self.file_path = "products_database.json"    
        self.load_data()

    ## to load data from json    
    def load_data(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as file:
                    all_data = json.load(file)
                    
                    if self.category in all_data:
                        category_data = all_data[self.category]
                        for item in category_data:
                            self.products.append(Products.from_dict(item))
            ## for json syntax error
            except json.JSONDecodeError:
                print("Your JSON has syntax error. i.e you messed up a comma or doublecollon or stuff that should be in JSON")
                sys.exit()
        else:
            print("No data found")
            self.products = []

    ## to save data to json    
    def save_data(self):
        try:
            all_data = {}

            if os.path.exists(self.file_path):
                with open(self.file_path, "r") as file:
                    all_data = json.load(file)
                
            all_data[self.category] = [product.to_dict() for product in self.products]

            with open(self.file_path, "w") as file:
                json.dump(all_data, file, indent=4)

        ## the e shows up the exception error
        except Exception as e:
            print(f"Error saving data: {e}")
    ## to add product    
    def add_product(self, product):
        if product.category.lower() == self.category.lower():
            # Check for duplicate product ID
            for existing_product in self.products:
                if existing_product.product_id == product.product_id:
                    print(f"Product ID {product.product_id} already exists in {self.category}")
                    return False
            self.products.append(product)
            self.save_data()
            print(f"Added {product.name} to {self.category}")
            return True
        else:
            print(f"Product {product.name} doesn't belong to {self.category}")
            return False
    ## to remove product
    def remove_product(self, product):
        for item in self.products:
            if item.product_id == product.product_id:
                self.products.remove(item)
                print(f"Removed {item.name} from {self.category}")
                self.save_data()
                return
        print(f"Product ID {product.product_id} not found in {self.category}")

    ## abstract method used cus there are many variants of tax calculation
    @abstractmethod
    def calc_tax(self):
        pass
    
    def display_products(self):
        for product in self.products:
            print(product)
    
## here in all classes the calc_tax method is implemented differently with initializing from parent class
class Electronics(Items):   
    def __init__(self):
        super().__init__("electronics")

    def calc_tax(self):
        return 0.10
    
class Stationaries(Items):
    def __init__(self):
        super().__init__("stationaries")
    def calc_tax(self):
        return 0.05
    
class Textiles(Items):
    def __init__(self):
        super().__init__("textiles")
    def calc_tax(self):
        return 0.08
    
class Books(Items):   
    def __init__(self):
        super().__init__("books")
    def calc_tax(self):
        return 0.02

class Grocery(Items):
    def __init__(self):
        super().__init__("grocery")
    def calc_tax(self):
        return 0.03