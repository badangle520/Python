#File name = c09_shuixianhuashu.py

num = range(100,1000)

for i in num:
    sum = 0
    temp = i
    while temp:
        sum +=  (temp%10) ** 3
        temp //= 10
    if sum == i:
        print(i)
