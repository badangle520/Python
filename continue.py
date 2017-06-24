#File name:continue.py

while True:
    s = raw_input('Enter something:')
    if s == 'quit':
	break
    if len(s) < 3:
	print 'Input is not sufficient length'
	continue
    else:
	print 'Input length is:', len(s)
