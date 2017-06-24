#File name = reference.py

print 'Simple Assignment' 
shoplist = ['a','b','c','d']
print 'original shoplist is',shoplist
mylist = shoplist
print 'original mylist is',mylist

print 'bought a now, my shoplist changed'
del mylist[0]
print 'shoplist is',shoplist
print 'mylist is',mylist

print 'copy by making a full slice'
mylist = shoplist[:]
print 'shoplist is',shoplist
print 'mylist is',mylist

print 'delete mylist[0] then'
del shoplist[0]
print 'shoplist is',shoplist
print 'mylist is',mylist
