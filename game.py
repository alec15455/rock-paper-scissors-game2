# game.py

import random
from dotenv import load_dotenv

load_dotenv()
user_name = os.getenv("PLAYER_NAME", default = "default")

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

if (computer_choice == user_choice) :
    result = tie
        print ("TIE!")
elif ((user_choice == "rock") and (computer_choice == "scissors")) :
    result = user_wins
        print("YOU WIN!")
elif ((user_choice == "scissors") and (computer_choice == "rock")) :
    result = computer_wins
        print("YOU LOSE!")
elif ((user_choice == "rock") and (computer_choice == "paper")) :
    result = user_wins
        print("YOU WIN!")
elif ((user_choice == "paper") and (computer_choice == "rock")) :
    result = computer_wins
        print("YOU LOSE!")
elif ((user_choice == "scissors") and (computer_choice == "paper")) :
    result = user_wins
        print("YOU WIN!")
elif ((user_choice == "paper") and (computer_choice == "scissors")) :
    result = computer_wins
        print("YOU LOSE!")
else:
    print("Please enter rock, paper, or scissors")
exit()