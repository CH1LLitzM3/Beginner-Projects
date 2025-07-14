import random

print("welcome to rock paper scissors\nquit using \"quit\"")
while True:
    exit_command = "quit"

    rock = "rock"
    paper = "paper"
    scissors = "scissors"

    user_choice = input("you choose: ").lower()
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
    elif comp_choice == rock and user_choice == scissors:
        print("comp wins!")
    elif comp_choice == paper and user_choice == rock:
        print("comp wins!")
    elif comp_choice == scissors and user_choice == paper:
        print("comp wins!")
    elif user_choice != exit_command or not rock or not paper or not scissors:
        print("play properly :(")

    if user_choice == "quit":
        print("exit success")
        break













