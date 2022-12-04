import sqlite3
from string import Template as tem

sql = ('''
SELECT UserName FROM USERS;
''')
database = sqlite3.connect("flaskr/database.db")
cur = database.cursor()
res = cur.execute(sql)
usernames = res.fetchall()
for i in usernames:
    print(i)