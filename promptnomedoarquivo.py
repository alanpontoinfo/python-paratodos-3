fname = input('Entre o nome do arquivo: ')
try:
    fhand = open(fname)
except:
    print('Arquivo não pode ser aberto:', fname)
    quit()
    
count=0
for line in fhand:
 if line.startswith('Assunto:') :
  count = count + 1
print('Existe', count, 'assunto linhas em', fname)