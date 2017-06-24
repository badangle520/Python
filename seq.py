#File name = seq.py

shoplist = ['a','b','c','d']

#index or subscription
print 'item 0 is',shoplist[0]
print 'item 1 is',shoplist[1]
print 'item 2 is',shoplist[2]
print 'item 3 is',shoplist[3]
print 'item -1 is',shoplist[-1]
print 'item -2 is',shoplist[-2]

#slicing on a list
print 'item 1 to 3 is',shoplist[1:3]
print 'item 2 to end is',shoplist[2:]
print 'item 1 to -1 is',shoplist[1:-1]
print 'item start to end is', shoplist[:]

#slcing on a string
name = 'david'
print 'characters 1 to 3 is', name[1:3]
print 'characters 2 to end is', name[2:]
print 'characters 1 to -1 is', name[1:-1]
print 'characters start to end is', name[:]
