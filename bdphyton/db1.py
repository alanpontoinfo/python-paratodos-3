import sqlite3
conn = sqlite3.connect('musicadb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Trilhas')
cur.execute('CREATE TABLE Trilhas (titulo TEXT, plays INTEGER)')
conn.close()