# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

# PROMP USER FOR INPUT

#x = input("Choose 'rock' or 'paper' or 'scissors'")
user_choice = input("Choose 'rock' or 'paper' or 'scissors':")
print(user_choice)

# COMPUTER CHOICE (AT RANDOM)

options = ["rock", "paper", "scissors"]

computer_chocie = random.choice(options)
print(computer_choice)
