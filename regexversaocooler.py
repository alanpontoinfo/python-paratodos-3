import re
lin = 'De alansantos@aprendendopyton.uf.edu Sab Jan 5 09:14:16 2022' 
y = re.findall('^De .*@([^ ]*)', lin)
print(y)


# '^De .*@ ([^ ]*)' inicia no começo da linha, procura pelo string 'De'

