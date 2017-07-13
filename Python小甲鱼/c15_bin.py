while True:
    temp = input('pls enter a num for binary conversion: ')
    if temp != 'quit':
        num = int(temp)
        print('10 -> 16 : %d -> %#x ' % (num,num))
        print('10 ->  8 : %d -> %#o ' % (num,num))
        print('10 ->  2 : %d ->' % num, bin(num))
    else:
        break
