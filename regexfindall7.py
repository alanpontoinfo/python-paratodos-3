import re

x= 'Nos apenas recebemos R$10.00 pelos bolos'
y = re.findall('/*R\$[0-9.]+', x)
print(y)