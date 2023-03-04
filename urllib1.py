# Desde Http é assim comum, Temos uma biblioteca que faz todo trabalho de socket para nós e faz a pagina web parecer um arquuivo

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

    # funciona de maneira parecida ao coma do curl