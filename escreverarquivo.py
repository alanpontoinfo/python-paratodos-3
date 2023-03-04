fout = open('escreverarquivo.txt', 'w')
print(fout)
linha1 = 'Este aqui e a primeira linhaescrita,\n'
fout.write(linha1)
linha2 = 'Este aqui e a segunda linhaescrita,\n'
fout.write(linha2)
fout.close()
