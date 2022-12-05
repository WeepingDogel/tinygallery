# The Authentication of the Users
import os
import sqlite3
import time
from flask import Flask
from flask import request
from flask import render_template
from flask import flash
from flask import session
from flask import redirect
from flask import url_for
from markupsafe import escape
from string import Template as tem

def auth():
    database = sqlite3.connect("flaskr/database.db")
    cur = database.cursor()
    Authen = tem('''
    SELECT * FROM USERS WHERE UserName LIKE "$username";
    ''')
    if request.method == 'POST':
        userName = request.form['username']
        passWord = request.form['password']
        res = cur.execute(Authen.substitute(username=userName)).fetchone()
        if res == None:
            return "用户名不存在"
        else:
            if userName == res[1] and passWord == res[2]:
                session['username'] = userName
                return redirect(url_for("index"))
                # return render_template("index.html", username = userName, var="none")
            else:
                return "登录失败，用户名或密码错误"
            