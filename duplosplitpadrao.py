line = 'Para :	alanpontoinfo@gmail.com Criado em:	20 de julho de 2022 09:01 testando o arquivo'

palavras = line.split()
email = palavras[2]
print(email)
pedacos = email.split('@')
print(pedacos)
print(pedacos[1])