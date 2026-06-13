import os
import json
import sys
from abc import ABC , abstractmethod

class products:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.quantity = 0
    
    def __str__(self):
        return f"{self.name} - ${self.price} (ID: {self.product_id})"

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "quantity": self.quantity
        }
    
    @staticmethod
    def from_dict(data):
        return products(data["product_id"], data["name"], data["price"], data["category"])
    

class items(ABC):
    
    def __init__(self , category):
        self.category = category
        self.products = []
        self.file_path = "products_database.json"    
        self.load_data()

        
    def load_data(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as file:
                    all_data = json.load(file)
                    
                    if self.category in all_data:
                        category_data = all_data[self.category]
                        for item in category_data:
                            self.products.append(products.from_dict(item))
            except json.JSONDecodeError:
                print("Your JSON has syntax error. i.e you messed up a comma or doublecollon or stuff that should be in JSON")
                sys.exit()
        else:
            print("No data found")
            self.products = []
        
    def save_data(self):
        try:
            all_data = {}

            if os.path.exists(self.file_path):
                with open(self.file_path, "r") as file:
                    all_data = json.load(file)
                
            all_data[self.category] = [product.to_dict() for product in self.products]

            with open(self.file_path, "w") as file:
                json.dump(all_data, file, indent=4)

        except Exception as e:
            print(f"Error saving data: {e}")
        
    def add_product(self, product):
        if product.category.lower() == self.category.lower():
            self.products.append(product)
            print(f"Added {product.name} to {self.category}")
            return True
        else:
            print(f"Product {product.name} doesn't belong to {self.category}")
            return False
    
    def remove_product(self, product):
        for item in self.products:
            if item.product_id == product.product_id:
                self.products.remove(item)
                print(f"Removed {item.name} from {self.category}")
                self.save_data()
                return
        print(f"Product ID {product.product_id} not found in {self.category}")

    @abstractmethod
    def calc_tax(self):
        pass
    

class electronics(items):   
    def __init__(self):
        super().__init__("electronics")

    def calc_tax(self):
        return 0.10
    
class stationaries(items):
    def __init__(self):
        super().__init__("stationaries")
    def calc_tax(self):
        return 0.05
    
class textiles(items):
    def __init__(self):
        super().__init__("textiles")
    def calc_tax(self):
        return 0.08
    
class books(items):   
    def __init__(self):
        super().__init__("books")
    def calc_tax(self):
        return 0.02

class grocery(items):
    def __init__(self):
        super().__init__("grocery")
    def calc_tax(self):
        return 0.03