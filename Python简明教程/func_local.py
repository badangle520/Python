#File name: local.py

def func(x):
    print 'x is', x
    x = 2
    print 'changed local x to', x

x = 50
func(x)
print 'current x is ', x
