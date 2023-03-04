# Desde Http é assim comum, Temos uma biblioteca que faz todo trabalho de socket para nós e faz a pagina web parecer um arquuivo

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    
    words= line.decode().split()
    for word in words :
         counts[word] = counts.get(word, 0) + 1
print(counts)         
         