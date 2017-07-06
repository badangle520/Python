#File name = c05_leapyear.py

running = True
times = 3

while running and times > 0 :
    temp = input("pls enter year and we will check if it's leap year: ")
    if temp.isdigit():
        year = int(temp)
        times -= 1
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
            print('your input year is leap year.')
        else:
            print('your input year is not leap year')
    else:
        print('your input is not number')
        times -= 1
        break

    if times == 0:
        print('game over!')
