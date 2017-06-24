#File name: global.py

def func():
    global x
    print 'x is', x
    x = 2
    print 'Changed local x to', x

x = 50
func()
print 'global value of x is', x
