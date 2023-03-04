print(ord('H'))
print(ord('e'))
print(ord('\n'))


#cada caracter is representado por um numero entre 0 e 256 armazenado em 8 bits de memoria
# Referimos para 8 bitis de memoria como 1 byte de memoria
# A funcao ord() conta-nos o valor numerico de uma simples caracter ASCII

# Multi-Byte Caracteres

#Para representar o largo alcance de caracters computadores devemos manipular a representaçao dos caracteres com mais do que 1 byte
# UTF-16 -> Tamanh fixado - dois bytes
# UTF-32 -> Tamanho fixado - 4 bytes
# UTF-8 -> 1.4 bytes
# Compativel com ASCII
# detecção Automática entre ASCII e UTF-8
# UTF-8 é recomendado para codificar dados para serem trocados entre sistemas