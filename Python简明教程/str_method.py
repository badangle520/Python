#File name = str_method.py

name = 'david' 

if name.startswith('dav'):
    print "Yes, the string starts with 'dav'"
if 'a' in name:
    print "Yes, the string contains 'a'"
if name.find('vi') != -1:
    print "Yes, the string contains 'vi'"

delimiter = '_*_'
mylist = ['a','b','c','d']
print delimiter.join(mylist)
