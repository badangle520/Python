nums = '0123456789'
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''

password = input('pls create password: ')
length = len(password)
flag_cnt = 0

while (length == 0) or (password.isspace == True):
    print('your enter password is empty or space, pls enter again: ')

if length <=8:
    flag_len = 1
elif 8 < length < 16:
    flag_len = 2
else:
    flag_len = 3

for each in password:
    if each in symbols:
        flag_cnt += 1
        break

for each in password:
    if each in chars:
        flag_cnt += 1
        break

for each in password:
    if each in nums:
        flag_cnt += 1
        break

while 1:
    print('your password security level: ')

    if flag_len == 1 or flag_con == 1:
        print('low')
        break
    if flag_len == 2 or flag_con == 2:
        print('mediume')
        break
    else:
        print('high')
        break
