#file name = c08_score.py

while True:
    temp = input('please enter score: ')
    score = int(temp)
    if  70 <= score < 80:
        print('C')
    elif 80 <= score < 90:
        print('B')
    elif 90 <= score <= 100:
        print('A')
    elif 60 <= score < 70:
        print('D')
    elif 0 <= score < 60:
        print('E')
    else:
        print('input error')
