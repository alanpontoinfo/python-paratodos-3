counts = dict()

print('Entre com a linha de texto:')

line = input('')

words = line.split()
print('Words:', words)

for word in words:
  counts[word] = counts.get(word, 0) + 1

  print('Counts', counts)
