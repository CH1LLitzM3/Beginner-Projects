import random

def rng_0to10():
    print("rng 0 to 10 \ntype \"0\" to exit")
    while True:
        command = input("\namount of numbers: ")
        try:
            command = int(command)
        except ValueError:
            print("not a number")
            continue
        for x in range(command):
            print(random.randint(0, 10))
        if command == 0:
            print("exit successful")
            break


print(rng_0to10())
