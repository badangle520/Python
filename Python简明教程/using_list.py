#File name = using_list.py

shoplist = ['b','d','c','a']
print 'I have',len(shoplist),'items to buy'
print 'these items are'
for item in shoplist:
    print item,

print '\nl also have to buy e.'
shoplist.append('e')
print 'now my shopping list change to',shoplist

shoplist.sort()
print 'I will sort my shopping list, after that it will be',shoplist

print 'The 1st item a have been bought'
del shoplist[0]
print 'currently, my shopping list change to',shoplist
