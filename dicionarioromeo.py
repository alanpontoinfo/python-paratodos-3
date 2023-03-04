fname = input('Entre com o nome do Arquivo:')
try:
    fhand = open(fname)
except:
     print('Arquivo não pode ser aberto:', fname)
     exit()

counts = dict()
for line in fhand:
     palavras = line.split()
     for palavra in palavras:
         if palavra not in counts:
          counts[palavra] = 1
         else:
          counts[palavra] += 1
print(counts)
