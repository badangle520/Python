#File name = c06_odd.py

number = 0

while number <= 100:
    if number % 2 == 0:
        number += 1
    else:
        print(number, end=' ')
        number += 1
