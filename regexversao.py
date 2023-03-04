#data = 'De alansantos@aprendendopyton.uf.edu Sab Jan 5 09:14:16 2022'

import re
lin = 'De alansantos@aprendendopyton.uf.edu Sab Jan 5 09:14:16 2022' 
y = re.findall('@([^ ]*)', lin)
print(y)

#'@([^ ]*)' Procurar atraves da string ate voce encontrar em um sinal - corresponde a caracter não branco - muitos deles