import re
x = 'My 2 favorite number are 3 e 9 '
y = re.findall('[0-9]+', x)
print(y)

y = re.findall('[AEIOU]+', x)
print(y)