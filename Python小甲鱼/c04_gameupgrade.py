#Filename = game.py

import random as r

times = 3
secret = r.randint(1,30)

print('Welcome to game: guess number between 1 and 30: ')

while True and times > 0 :
    temp = input("please enter num: ")
    guess = int(temp)
    times -= 1

    if guess == secret:
        print ("Congratulations, your are correct!\n")
        break
    elif guess > secret:
        print("pls enter smaller number: ")
    else:
        print("pls enter bigger number: ")

    if times == 0:
        print("Game Over")
