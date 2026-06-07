##this is a program to guess the correct number
import random

##global values
t_num = random.randint(1, 100)
guess = 0
max_guess = 10

print("Welcome to the Number Guessing Game!")
print(f"You have {max_guess} guesses to guess the number between 1 and 100.")

#idk if the try method is required but I'm learning it so I'll "try" it heh
while guess < max_guess:
    try:
        guess = int(input("Enter your guess: "))
        guess += 1
        if guess < t_num:
            print("Too low! Try again.")
        elif guess > t_num:
            print("Too high! Try again.")
        else:
            print(f"That's the number! You guessed the number in {guess} guesses.")
            break
    except ValueError:
        print("Please enter a valid number.")
if guess == max_guess:
    print(f"Guesses are over buddy! The number was {t_num}.")
    