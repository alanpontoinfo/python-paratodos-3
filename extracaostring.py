# voce pode refina a match para re.findall() e sepparadamente deteminar qual porção do match épara ser extraido por usar parenteses

import re
texto = 'De alanpontoinfo@gmail.com Sab jan 21 16:25:30 2022'

y = re.findall('\S+@\S+', texto)
print(y)


z = re.findall('^De (\S+@\S+)', texto)
print(z)
# \S+@\S+ pelo menos um  caracter espaço não branco

# (\S+@\S+) parenteses não são parte do match - mas les contam onde inicia e para  que string extarir