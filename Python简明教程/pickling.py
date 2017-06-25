#Filename: pickling.py

import cPickle as p                # import pickle as p
shoplistfile = 'shoplist.data'  # the file name used to store the object
shoplist = ['a', 'b', 'c']


# Write to the file
f = file(shoplistfile, 'w')
p.dump(shoplist,f)              # dump the object to a file
f.close()

# remove the shoplist
del shoplist

# Read back from the storage
f = file(shoplistfile)
storedlist = p.load(f)
print storedlist
