class Instruments:
    def __init__(self):
        self.sound = "Playing instrument"
    
    def play(self):
        print(self.sound)
    
class Guitar(Instruments):
    def __init__(self):
        super().__init__()
        self.sound = "Playing guitar"
    
    def play(self):
        print(self.sound)
    
class Piano(Instruments):
    def __init__(self):
        super().__init__()
        self.sound = "Playing piano"
    
    def play(self):
        print(self.sound)

class Violin(Instruments):
    def __init__(self):
        super().__init__()
        self.sound = "Playing violin"
    
    def play(self):
        print(self.sound)

def main():
    playing = input("Choose your instrument:").lower().strip()
    
    if playing == "guitar":
        guitar = Guitar()
        guitar.play()
    elif playing == "piano":
        piano = Piano()
        piano.play()
    elif playing == "violin":
        violin = Violin()
        violin.play()
    else:
        print("Invalid instrument")

if __name__ == "__main__":
    main()
