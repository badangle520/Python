#File name = c09_password.py

times = 3
asterisk = 0
password = 'abc123'

while True:
    temp = input('pls enter password: ')

    if temp == password:
        print('password correct, enter program..')
        break
    elif '*' in temp:
        print("your password contain invalid sign '*'")
    else:
        times -= 1
        print("your password enter wrong, you have ",times,"more chance")

    if times == 0:
        print("your error times up to 3, id has been lock")
        break
