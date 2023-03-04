line = 'A quantidade            de espacos'
etc = line.split()
print(etc)

line = 'primeiro;segundo;terceiro'
thing = line.split()
print(thing)
print(len(thing))
thing = line.split(';')
print(thing)
print(len(thing))