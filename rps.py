import random

options = ["rock", "paper", "scissors"]
computer = random.choice(options)
user = input("Enter rock, paper, or scissors: ").lower()

print(f"Computer chose: {computer}")

if user == computer:
    print("It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("You win! Rock smashes Scissors.")
    else:
        print("You lose! Paper covers Rock.")
elif user == "paper": # Added colon
    if computer == "rock": # Added colon
        print("You win! Paper covers rock.")
    else:
        print("You lose! Scissors cut the paper.")
elif user == "scissors": # Added colon
    if computer == "paper": # Added colon
        print("You win! Scissors cut the paper.")
    else:
        print("You lose! Rock smashes Scissors.")