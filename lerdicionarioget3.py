fname = input('Entre com o arquivo:')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname) 

di = dict()
for lin in hand:
    lin = lin.rstrip()
    
    wds = lin.split()
    
    
    for w in wds:
     #idiom: recupera/cria/atualoza contador
     di[w]= di.get(w,0) + 1
    # print(w, 'new', di[w])
#print(di)

#agoa queremos encontrar a palavra mais comum
maislargo = -1
apalavra = None
for k,v in di.items() :
    print(k,v)
    if v > maislargo :
         maislargo = v
         apalavra = k # lembra a palavra que foi mais largo
print('Feito', apalavra, maislargo)        