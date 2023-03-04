# Os caracteres repetidos (* e +) push para fora em ambras direçoes(greedy) para corresponder o maior string possivel

import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

# ^F Primeiro caracter em corresponcia é um F
# .+ Um ou mais caracteres
# Ultimu caractere na correspondencia é um :