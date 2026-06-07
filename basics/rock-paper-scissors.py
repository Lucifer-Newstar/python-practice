#this is a program to play rock paper scissors with the computer
import random
#global values
user_points = 0
computer_points = 0
ties = 0
options = ["rock", "paper", "scissors"]

##loop for game till quiting
while True:

    #user choice
    choice = input("Enter a choice (rock, paper, scissors): ").lower()
    #computer choice
    computer_choice = random.choice(options)

    print(f"You chose {choice} and the computer chose {computer_choice}")

    if computer_choice == choice:
        print("It's a tie")
        ties += 1

    elif computer_choice == "rock" and choice == "paper":
        user_points += 1

    elif computer_choice == "rock" and choice == "scissors":
        computer_points += 1

    elif computer_choice == "paper" and choice == "rock":
        computer_points += 1

    elif computer_choice == "paper" and choice == "scissors":
        user_points += 1

    elif computer_choice == "scissors" and choice == "rock":
        user_points += 1

    elif computer_choice == "scissors" and choice == "paper":
        computer_points += 1
    
    else:
        print("Invalid Choice")
    
    print (f"Your points is {user_points}. Computer points is {computer_points}. No.of.Ties is {ties}. To exit press esc")
    #to continue playing or exit
    play_again = input("To continue playing press Enter, to exit type 'esc': ").lower()
    #to exit the game
    if play_again == "esc":
        print ("Thanks for playing!")   
        break