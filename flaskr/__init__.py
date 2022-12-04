# TinyGalley
# By WeepingDogel

import os
import sqlite3
import time
from flask import Flask
from flask import request
from flask import render_template
from markupsafe import escape
from string import Template as tem

app = Flask(__name__)
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/login_and_register")
def login_and_register():
    return render_template("auth/login_and_register.html")

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        userName = request.form['username']
        passWord = request.form['password']
        
    return render_template('auth/login_and_register.html')

@app.route('/register', methods=['GET','POST'])
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