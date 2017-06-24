#File name:while.py

number = 23
running = True

while running:
    guess = int(raw_input('Enter an integer:'))
    
    if guess == number:
        print 'Congratuations, you guessd it.'
        running = False
    elif guess > number:
        print 'Sorry, you guess wrong, it is a little lower than that.'
    else:
        print 'Sorry, you guess wrong, it is a little lower than that.'
else:
    print 'The while loop is over.'

print 'Done'
