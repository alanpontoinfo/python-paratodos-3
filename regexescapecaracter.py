import re
x='We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y)

# Se voce quer um especial caracter regular expression apenas comporte normalmente( maioria das vezes) voce prefixa o com '\'

#\$[0-9.]+ um real sinal de dolar - um digito ou periodo - pelo menos um ou mais