#encontra valor acima de 10

counts = { 'chuck': 1, 'ane': 42, 'jan':100}
for key in counts:
     if counts[key] > 10:
          print(key, counts[key])