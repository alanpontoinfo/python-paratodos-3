count = 0
sum = 0

print('Antes', count, sum)
for valor in [9, 41, 12, 3, 74, 15] :
 count = count + 1
 sum = sum + valor
 print(count, sum, valor)
 print('Depois', count, sum, sum/count)