str1 = 'iloveyou'
print(str1[0])
print(list(str1))
print(str1[1:3])
print(min(str1))

list1 = [1, 2, 3, 4, 5]
print(list1[1])
print(list(list1))
print(list1[0:])
print(max(list1))
print(sum(list1))
print(sum(list1,5))

turple1 = (6, 7, 8, 9, 10)
print(turple1[2])
print(list(turple1))
print(turple1[2:])

list2 = [1, 7, 3, 8, 2, 16, 9]
print(sorted(list2))
print(sorted(list2,reverse=True))
print(list(reversed(list2)))

list3 = ['c','a','b']
print(list(enumerate(list3)))

list4 = ['x','y','z','p','q']
print(list(zip(list3,list4)))
