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


user_wins = "YOU WIN!"
computer_wins = "YOU LOSE!"
tie = "TIE!"

if (computer_choice == user_choice) :
    print ("TIE!")
elif ((user_choice == "rock") and (computer_choice == "scissors")) :
    print("YOU WIN!")
elif ((user_choice == "scissors") and (computer_choice == "rock")) :
    print("YOU LOSE!")
elif ((user_choice == "rock") and (computer_choice == "paper")) :
    print("YOU WIN!")
elif ((user_choice == "paper") and (computer_choice == "rock")) :
    print("YOU LOSE!")
elif ((user_choice == "scissors") and (computer_choice == "paper")) :
    print("YOU WIN!")
elif ((user_choice == "paper") and (computer_choice == "scissors")) :
    print("YOU LOSE!")
else:
    print("Please enter rock, paper, or scissors")
exit()