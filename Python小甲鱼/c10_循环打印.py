member = ['a',88,'b',90,'c',85,'d',90,'e',88]

for each in member:
    print(each,end= ' ')

count = 0
length = len(member)
while count < length:
    print(member[count], member[count+1])
    count += 2

for each in range(len(member)):
    if each%2 ==0:
        print(member[each], member[each+1])
