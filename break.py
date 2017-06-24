#File name:break.py

while True:
    s = raw_input('Enter something:')
    if s == 'quit':
	break
    print 'length of the string is:', len(s)
print 'Done'
