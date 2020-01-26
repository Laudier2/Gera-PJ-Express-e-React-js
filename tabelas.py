import sqlite3

con = sqlite3.connect('Database.db')
cur = con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cur.fetchall()
for p in tabelas:
    print(p[0])