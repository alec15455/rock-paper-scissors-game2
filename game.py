# game.py

user_name = os.getenv ("PLAYER_NAME", default = "PLAYER")
print("Welcome {user_name}")

user_choice = input("Choose 'rock' or 'paper' or 'scissors':")
print("YOU CHOSE!")
print(user_choice)

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer chose:")

print(computer_choice)

if user_choice == computer_choice:
    print ("TIE!")

if user_choice == "rock":
    if computer_choice == "rock":
        print("YOU LOSE!")
    elif computer_choice == "paper":
        print("YOU LOSE!")
    elif computer_choice == "scissors":
        print("YOU WIN!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("YOU WIN!")
    elif computer_choice == "paper":
        print("YOU LOSE!")
    elif computer_choice == "scissors":
        print("YOU LOSE!")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("YOU LOSE!")
    elif computer_choice == "paper":
        print("YOU WIN!")
    elif computer_choice == "scissors":
        print("YOU LOSE!")
else:
    print("Please enter rock, paper, or scissors")
exit()