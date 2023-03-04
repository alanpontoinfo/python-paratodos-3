d={'b': 1, 'a': 10,  'c':22}
tmp = list() 
for k,v in d.items() :
    tmp.append((v,k))

print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)    