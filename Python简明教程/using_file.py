#File name = using_file.py

poem = '''\
test
'''

f = file('poem.txt','w')#open for 'w'riting
f.write(poem)		#write text to file
f.close()		#close the file	

f = file('poem.txt')
#if no mode is specified, 'r'ead mode is assumed by default
while True:
    line = f.readline()
    if len(line) == 0:	#Zero length indicated EOF
	break
    print line,	#Notice comma to avoid automatic nreline added by python
f.close() #close the file
