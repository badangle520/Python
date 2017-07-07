print('''
list1 = [x**2 for x in range(5)]
print(list1)
''')

list1 = [x**2 for x in range(5)]
print(list1)

list2 = ['1.just do it',               \
         '2.everything is possiable',  \
         '3.coding change the world']

list3 = ['3.Fishc', \
         '1.NIKE',  \
         '2.LINING']

list4 = [name + ':  \t' + slogan[2:] for slogan in list2 for name in list3 if name[0] == slogan[0]]
for each in list4:
    print(each)
