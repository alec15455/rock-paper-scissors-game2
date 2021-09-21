# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

# PROMP USER FOR INPUT

#x = input("Choose 'rock' or 'paper' or 'scissors'")
user_choice = input("Choose 'rock' or 'paper' or 'scissors':")
print(user_choice)

# COMPUTER CHOICE (AT RANDOM)

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer chose:")
print(computer_choice)


user_wins = "YOU WIN!"
computer_wins= "YOU LOSE!"
tie = "TIE!"

if (computer_choice == user_choice) :
    result = tie
elif ((user_choice == "rock") and (computer_choice == "scissors")) :
    result = user_wins
elif ((user_choice == "scissors") and (computer_choice == "rock")) :
    result = computer_wins
elif ((user_choice == "rock") and (computer_choice == "paper")) :
    result = user_wins
elif ((user_choice == "paper") and (computer_choice == "rock")) :
    result = computer_wins
elif ((user_choice == "scissors") and (computer_choice == "paper")) :
    result = user_wins
elif ((user_choice == "paper") and (computer_choice == "scissors")) :
    result = computer_wins

print("THANKS PLEASE PLAY AGAIN")