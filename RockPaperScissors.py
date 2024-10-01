import random

user_choice = int(input("Welcome to the game. Choose rock, paper or scissors\n"))
computer_choice = random.randint(0 , 2)
# Building the main function of the program

if user_choice >= 3 or user_choice < 0:
    print("Invalid number, try again!")
if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice == computer_choice:
    print("It's a draw")
elif user_choice > computer_choice:
    print("You win")