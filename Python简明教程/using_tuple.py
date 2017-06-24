#File name = using_tuple.py

zoo = ('c','a','b')
print 'No. of animals in the old zoo is',len(zoo)

new_zoo = ('e','d',zoo)
print 'No. of animals in the new zoo is',len(new_zoo)
print 'all the animals in the zoo are',new_zoo
print 'Animals from old zoo are',new_zoo[2]
print 'the last anmial bought from old zoo is',new_zoo[2][2]
