import sqlite3
conn = sqlite3.connect('musicadb.sqlite')
cur = conn.cursor()

cur.execute('INSERT INTO Trilhas (titulo, plays) VALUES (?, ?)',
('Thunderstruck', 20))
cur.execute('INSERT INTO Trilhas (titulo, plays) VALUES (?, ?)',
('My Way', 15))
conn.commit()
print('Trilhas:')
cur.execute('SELECT titulo, plays FROM Trilhas')
for row in cur:
 print(row)
 #cur.execute('DELETE FROM Trilhas WHERE plays < 100')
conn.commit()
cur.close()