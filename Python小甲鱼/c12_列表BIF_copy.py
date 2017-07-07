print('''
list1 = [123, 456]
list2 = list1.copy()
print(list2)
''')

list1 = [123, 456]
list2 = list1.copy()
print(list2)

print('''
list3 = [3, 4, 5]
list4 = list3
list5 = list3.copy()
list3.append('happy')
print(list3)
print(list4)
print(list5)
''')

list3 = [3, 4, 5]
list4 = list3
list5 = list3.copy()
list3.append('happy')
print(list3)
print(list4)
print(list5)
