palavra = 'brontossauro'
d= dict()
for c in palavra:
     if c not in d:
          d[c]=1
     else:
           d[c] = d[c]  + 1
print(d)         