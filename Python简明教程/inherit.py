#File name: inherit.py

class SchoolMember:
    '''Represent any school member.'''
    def __init__(self,name,age):
	self.name = name
	self.age = age
	print'(Initialized School Member: %s)' %self.name

    def tell(self):
	'''Tell my details'''
	print'Name. "%s" Age: "%s"' %(self.name,self.age),

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
	SchoolMember.__init__(self, name, age)
	self.salary = salary
	print'(Initialized Teacher: %s)' %self.name

    def tell(self):
	SchoolMember.tell(self)
	print'Salary: "%d"' %self.salary

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
	SchoolMember.__init__(self, name, age)
	self.marks = marks
	print'(Initialized Student: %s)' %self.name

    def tell(self):
	SchoolMember.tell(self)
	print'Marks: "%d"' %self.marks

t = Teacher('david',40,40000)
s = Student('tina',22,75)

print

members = [t,s]
for member in members:
    member.tell()
