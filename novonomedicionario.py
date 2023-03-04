counts = dict()

nomes = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

for nome in nomes :
    if nome not in counts:
     counts[nome] = 1
    else :
     counts[nome] = counts[nome] + 1
     print(counts)