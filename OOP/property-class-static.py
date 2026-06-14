class Product:
    platform = "Amazon"
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            self.__log_error(f"Price cannot be negative: {value}")
            raise ValueError("Enter a valid price")
        self._price = value
    
    def __log_error(self, message):
        print(f"Error: {message}")
    
    @classmethod
    def get_platform(cls):
        return cls.platform
    
    @staticmethod
    def get_tax(price):
        return price * 0.18
    
def main():
    product = Product("Laptop", 1000)
    print(product.price)
    product.price = 2000
    print(product.price)
    print(Product.get_platform())
    print(Product.get_tax(1000))
    
if __name__ == "__main__":
    main()