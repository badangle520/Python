#1
list1 = [1, [1, 2, ['aaa']], 3, 5, 8, 13, 18]
print(list1)
list1[1][2][0] = 'bbb'
print(list1)

#5
list2 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
print('list2 = ',list2)

list3 = []
for x in range(10):
    for y in range(10):
        if (x%2 == 0) and (y%2 != 0):
            list3.append((x,y))
print('list3 = ',list3)

#5
