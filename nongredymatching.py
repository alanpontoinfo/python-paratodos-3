# Nem todos codigos de expressao regulares que repete são greedy
# If voce adcionar um caracter ?, o + e * relaxa um pouco

import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)

# ^F Primeiro caracter em corresponcia é um F
# .+? Um ou mais caracteres mas não em ambas direçoes nongredy
# Ultimo caractere na correspondencia é um :