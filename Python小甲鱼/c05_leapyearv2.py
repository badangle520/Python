#File name = c05_leapyearv2.py

times = 3

while times > 0:
    temp = input('pls enter year:')
    times -= 1
    while not temp.isdigit():
        temp = input('sorry, your enter is wrong, pls enter number: ')

    year = int(temp)
    if year/400 == int(year/400):
        print('it is leap year..')
    else:
        if (year/4 == int(year/4)) and (year/100 != int(year/100)):
            print(temp + ' is leap year')
        else:
            print(temp + ' is not leap year')

    if times == 0:
        print('times up to 3..')
