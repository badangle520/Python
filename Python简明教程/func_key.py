#File name: func_key.py

def func(a,b=500,c=100):
    print 'a is',a,'\t',	\
          'b is',b,'\t',	\
          'c is',c

func(300,700)

func(250,c=240)

func(c=555,a=111)
