numlist = list()
while True :
 inp = input('Entre com o numero:')
 if inp =='feito' : break
 value = float(inp)
 numlist.append(value)

 media = sum(numlist) / len(numlist)
 print('Media:', media)