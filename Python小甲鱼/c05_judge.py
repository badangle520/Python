#File name = c05_judge.py

a = '111'
b = 'aaa'
c = 'AAA'
d = 'a1a'
e = 'A1A'
f = 'A1a'
g = 'a1A'

print('''
a = '111'
b = 'aaa'
c = 'AAA'
d = 'a1a'
e = 'A1a'
f = '  '
''')

print('print(a.isdigit())')
print(a.isdigit())

print('print(a.isalnum())')
print(a.isalnum())

print('print(b.isalpha())')
print(b.isalpha())

print('print(b.isalnum())')
print(b.isalnum())

print('print(b.islower())')
print(b.islower())

print('print(c.isupper())')
print(c.isupper())

print('print(d.isalnum())')
print(d.isalnum())

print('print(e.istitle())')
print(e.istitle())

print('print(f.isspace())')
print(f.isspace())

