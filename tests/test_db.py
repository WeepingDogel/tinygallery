import sqlite3
from string import Template as tem

sql = ('''
SELECT UserName FROM USERS;
''')
database = sqlite3.connect("flaskr/database.db")
cur = database.cursor()
Authen = cur.execute("SELECT UserName,PassWord FROM USERS;")
for i in Authen.fetchall():
    print(i)