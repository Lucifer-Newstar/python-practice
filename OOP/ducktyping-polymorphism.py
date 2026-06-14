class bike():
    def start(self):
        print("Starting a bike")
    
    def stop(self):
        print("Stopping a bike")

class car():
    def start(self):
        print("Starting a car")
    
    def stop(self):
        print("Stopping a car")

class truck():
    def start(self):
        print("Starting a truck")
    
    def stop(self):
        print("Stopping a truck")

class jetski():
    def start(self):
        print("Starting a jetski")
    
    def stop(self):
        print("Stopping a jetski")

class washingmachine():
    def start(self):
        print("Starting a washing machine")
    
    def stop(self):
        print("Stopping a washing machine")

def main():

    entities = [bike(), car(), truck(), jetski(), washingmachine()]
    
    ##implementing polymorphism
    for entity in entities:
        print(f"entity: {entity.__class__.__name__}")
        entity.start()
        entity.stop()
    
if __name__ == "__main__":
    main()

