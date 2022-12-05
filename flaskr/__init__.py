# TinyGalley
# By WeepingDogel
#

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

app = Flask(__name__)
app.secret_key = b'905bd5453270081b623caf48b2c59159b25121018a1bddeda190f9c4fa77e2a4'
@app.route("/")
@app.route("/index")
def index():
    if 'username' in session:
        return render_template("index.html", username = session['username'], var="none")
    else:
        return render_template("index.html")
@app.route("/login_and_register")
def login_and_register():
    return render_template("auth/login_and_register.html")

@app.route('/auth', methods=['GET', 'POST'])
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
            
@app.route('/register', methods=['GET','POST']) # Register 
def register():
    database = sqlite3.connect('flaskr/database.db')
    addUser = tem('''
INSERT INTO USERS(UserName, PassWord, Email, Date)
VALUES("$username", "$password", "$email", "$date");
    ''')
    if request.method == 'POST':
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        userName = request.form['userName_Register']
        passWord = request.form['passWord_Register']
        passWordRepeat = request.form['passWord_Repeat']
        Email = request.form['Email']
        if passWord == passWordRepeat:
            cur = database.cursor()
            cur.execute(addUser.substitute(username=userName, password=passWord, email=Email, date=date))
            database.commit()
            database.close()
            return "注册成功!"
        else:
            return "两次输入的密码不一致！"
            pass
    return render_template("auth/login_and_register.html")

@app.route("/Pics")
def Pics():
    return render_template("pics.html")