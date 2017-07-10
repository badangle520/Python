while True:
    type_psw = input('please choose the type of password you want to create: ')

    if type_psw != 'simple' or 'medium' or 'strong'
        print('invalid password type..')
        continue
    else:
        while True:
            psw = input('please create your password: ')
            if psw.isdigit() == True:
                print('password only number, pls add num & str')
                continue
            if psw.isalpha() == True:
                print('password only str, pls use num & str')
                continue
            if psw.isalnum() == True:
                    if len(psw) > 8:
                        print('invalid length for psw, should <= 8')
                        continue
                    else:
                        print('your password created successfully')
                        break
            else:
                print('password can only include num & str')
