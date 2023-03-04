fhand = open('teste.txt')
for line in fhand:
 line = line.rstrip()
 if not line.startswith('Para:') :
  continue
 print(line)