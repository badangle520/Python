#Filename=guess.py
import random

secret = random.randint(1,100)
running = True

while running:
    guess = int(input('pls input num to guess: '))

    if guess == secret:
        print('Your guess is correct, thank you for join the game!')
        while running:
            confirm = input('enter "quit" to leave or "continue" to play again: ')
            if confirm == 'quit':
                running = False
            elif confirm == 'continue':
                break
            else:
                print("you entered wrong action, pls re-enter again.")
                continue 
    elif guess > secret:
        print('pls enter smaller number and then try again: ')
    else:
        print('pls enter bigger number and then try again: ')

print('You have quit the game, welcome next time!')

