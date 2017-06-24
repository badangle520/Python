#file name: if.py

number = 23
guess = int(raw_input('Enter an integer:'))

if guess == number:
	print 'Congratulations, you guess it.'
	print "(but you do not with any prized)"
elif guess < number:
	print 'No, it is a little higher than that'
else:
	print 'NO, it is a little lower than that'
print 'Done'

