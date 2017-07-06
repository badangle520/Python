#File name = c06_step.py

a = 1
running = True

while running:
    if (a % 2 == 1) and  \
       (a % 3 == 2) and  \
       (a % 5 == 4) and  \
       (a % 6 == 5) and  \
       (a % 7 == 0):
        print(a)
        running = False
    else:
        a += 1
