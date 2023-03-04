fhand = open('teste.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('Para:'):
     print(line)