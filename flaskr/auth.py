# Authorization

import functools
import time
from flaskr.db import get_db
from flask import(
    Blueprint, 
    g, 
    redirect, 
    render_template, 
    request, session, 
    url_for,
    )

bp = Blueprint('auth', __name__, url_prefix = '/auth')

@bp.route("/register", methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        userName = request.form['username']
        passWord = request.form['password']
        repeatPassword = request.form['repeat_password']
        Email = request.form['email']
        Date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        db = get_db()
        if userName == "" or passWord == "" or Email == "":
            return "Username, password and email is required <a href='/login_and_register'>Back</a>"
        elif passWord == repeatPassword:
            try:
                db.execute("INSERT INTO USERS(UserName, PassWord, Email, Date) VALUES(?, ?, ?, ?)",(userName, passWord, Email, Date))
                db.commit()
                return redirect("/login_and_register")
            except db.IntegrityError:
                return "User has already existed. <a href='/login_and_register'>Back</a>"
        else:
            return "Passwords are different. <a href='/login_and_register'>Back</a>"

    # return "Passwords are different. <a href='/login_and_register'>Back</a>"
    # return redirect("/login_and_register")

@bp.route("/login")
def login():

    return "Login"