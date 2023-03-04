palavra = 'brontossauro'
d= dict()
for c in palavra:
    d[c] = d.get(c,0)+ 1
print(d)    