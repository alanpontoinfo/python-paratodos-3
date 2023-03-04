total = 0 
count = 0
while True :
  inp = input('Entre com um numero:')
  if inp == 'feito' : break
  valor = float(inp)
  total = total + valor
  count = count + 1  
  media = total / count
  print('Media:', media)