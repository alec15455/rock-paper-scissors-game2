# this is the game.py file

import random
from dotenv import load_dotenv
load_dotenv()

import os

name = os.getenv ("PLAYER_NAME", default= "PLAYER 1")
print("Welcome PLAYER 1 to my game")

user_choice = input("Please choose 'rock' or 'paper' or 'scissors':")
print("YOU CHOSE:")
print(user_choice)

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("COMPUTER CHOSE:")

print(computer_choice)

if user_choice == computer_choice:
    print ("TIE!")

if user_choice == "rock":
    if computer_choice == "paper":
        print("YOU LOSE!")
    elif computer_choice == "scissors":
        print("YOU WIN!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("YOU WIN!")
    elif computer_choice == "scissors":
        print("YOU LOSE!")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("YOU LOSE!")
    elif computer_choice == "paper":
        print("YOU WIN!")
else:
    print("Please enter rock, paper, or scissors!")
exit()