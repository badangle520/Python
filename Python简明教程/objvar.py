#File name = objvar.py

class Person():
    '''Represents a person.'''
    population =0
   
    def __init__(self,name):
	'''Initializes the person's data'''
	self.name = name
	print'(Initializing %s)' %self.name

	#when this person is created, he/she adds to population
	Person.population += 1

    def __del__(self):
	'''I am dying.'''
	print '%s says bye.' %self.name

	Person.population -= 1

	if Person.population == 0:
	    print 'I am the last one.'
	else:
	    print 'There are still %d prople left.' %Person.population

    def sayHi(self):
	'''Greeting by the person.

	Really, that,s all it does'''
	print'Hi, my name is %s.' %self.name

    def howMany(self):
	'''Prints the current population.'''
	if Person.population == 1:
	    print 'I am the only person here.'
	else:
	    print 'We have %d person here.' %Person.population

a = Person('david')
a.sayHi()
a.howMany()

b = Person('tina')
b.sayHi()
b.howMany()

a.sayHi()
a.howMany()
