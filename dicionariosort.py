
counts = { 'chuck': 1, 'ane': 42, 'jan':100}
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
     print(key, counts[key])