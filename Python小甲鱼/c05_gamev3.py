#Filename = c05_gamev3.py

import random as r

times = 3
secret = r.randint(1,30)
guess = 0

print('Welcome to game: guess number between 1 and 30: ')

while (guess != secret) and (times > 0) :
    temp = input()

    while not temp.isdigit():
        temp = input("sorry, your enter is not num, please enter again: ")

    guess = int(temp)
    times -= 1

    if guess == secret:
        print ("Congratulations, your are correct!\n")
    else:
        if guess > secret:
            print("your guess number is bigger..")
        else:
            print("your guess number is smaller..")

        if times != 0:
            print("please try again.. ")
        else:
            print("your chance has been used up..")

print("game over..")
