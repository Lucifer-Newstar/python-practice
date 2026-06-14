from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, initial_move):
        self._moves = initial_move

    def get_moves(self):
        return self._moves
    
    def set_moves(self, moves):
        valid_moves = ["Running", "Jumping"]
        if moves in valid_moves:
            self._moves = moves
        else:
            print(f"{self.__class__.__name__} cannot {moves}")
    
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self):
        super().__init__("Running")
    
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self):
        super().__init__("Jumping")
    
    def make_sound(self):
        return "Meow!"

def main():
    dog = Dog()
    cat = Cat()
    print(dog.make_sound())
    print(cat.make_sound())
    dog.set_moves("Swimming")
    cat.set_moves("Climbing")

if __name__ == "__main__":
    main()