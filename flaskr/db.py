# Initialize The DATABASE
import sqlite3
from string import Template as tem

database = sqlite3.connect("flaskr/database.db")
cur = database.cursor()
Authen = tem('''
SELECT * FROM USERS WHERE UserName LIKE "$username";
    ''')
res = cur.execute(Authen.substitute(username="WeepingDogel1")).fetchone()
print(res == None)