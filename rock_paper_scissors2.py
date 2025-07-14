import random
from os import replace

print("welcome to rock paper scissors\nquit using \"quit\"")
while True:
    exit_command = "quit"

    rock = "rock"
    paper = "paper"
    scissors = "scissors"

    user_choice = input("you choose: ")
    user_nochoice = not rock or not paper or not scissors

    comp_choice = random.choice([rock, paper, scissors])
    print(f"computer chose: {comp_choice}")

    if user_choice == comp_choice:
        print("draw!")
    elif user_choice == rock and comp_choice == scissors:
        print("player wins!")
    elif user_choice == paper and comp_choice == rock:
        print("player wins!")
    elif user_choice == scissors and comp_choice == paper:
        print("player wins!")
    elif user_choice != "quit" or not rock or not paper or not scissors:
        print("play properly :(")
    else:
        print("comp wins!")

    if user_choice == "quit":
        print("exit success")
        break













