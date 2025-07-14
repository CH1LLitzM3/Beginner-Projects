print("welcome to guess the number, simply guess the number between 1 and 10")

guess = int(input("guess: "))
quit = "quit"

while guess != 4:
    if guess == 69:
        print("hehe")
        guess = int(input("guess: "))
    elif guess > 10 or guess < 1 and not guess == 69:
        print(f"{guess} really?")
        guess = int(input("guess: "))
    elif guess != 4:
        print("no")
        guess = int(input("guess: "))
    elif guess == 4:
        break

print("nice man")

