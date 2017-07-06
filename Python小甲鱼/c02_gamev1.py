#Filename = game.py

print('Welcome to game: guess number between 1 and 100: ')
temp = input("please enter num: ")
guess = int(temp)
if guess == 8:
    print ("correct")
else:
    print("wrong")
print("game over")
