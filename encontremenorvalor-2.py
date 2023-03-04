menorvalor = None
print('Antes')
for valor in [ 9,4, 12, 3, 74, 15] : 
 if menorvalor is None :
   menorvalor = valor
 elif valor < menorvalor :
     menorvalor = valor
 print(menorvalor, valor)
 print('Depois', menorvalor)