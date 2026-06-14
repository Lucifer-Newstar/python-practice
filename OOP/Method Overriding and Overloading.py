class Parent:

    def greet(self):
        print("Greetings from Parent")

class Child(Parent):

    def greet(self):
        print("Usually no greetings from Child")
    
def add_numbers(*args):
    return sum(*args)

def add_numbers(a, b, c=None):
    if c is None:
        return a + b
    return a + b + c

if __name__ == "__main__":
    ##method overriding
    parent = Parent()
    parent.greet()
    
    child = Child()
    child.greet()
    
    ##method overloading(can't name two functions with same name)
    print(add_numbers(1, 2))
    print(add_numbers(1, 2, 3))
    