fhand = open('teste2.txt')
for line in fhand:
 line = line.rstrip()
 if not line.startswith('Para ') : continue
 palavras = line.split()
 print(palavras[7])