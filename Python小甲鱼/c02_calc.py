#Filename = c02_calc.py

print('Let\'s play a game to guess the specified number between 1 to 100')

user_input = input('Game starts, please enter a number: ')
number = int(user_input)

if number != 76:
    print('Sorry, please try again.')
else:
    print('Congratulations!')
