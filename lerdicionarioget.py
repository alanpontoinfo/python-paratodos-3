fname = input('Entre com o arquivo:')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname) 

di = dict()
for lin in hand:
    lin = lin.rstrip()
    
    wds = lin.split()
    
    
    for w in wds:
     # se key não estar lá  count é zero
         oldcount = di.get(w,0) 
         print(w, 'old', oldcount)
         newcount = oldcount + 1
         di[w] = newcount
         print(w, 'new', newcount)
     
     #   print('**',w,di.get(w,-99))
      #  if w in di :
       #    di[w] = di[w] + 1
          
       # else :
        #   di[w] = 1
          
       # print(w,di[w])
print(di)