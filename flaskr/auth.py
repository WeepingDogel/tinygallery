# Authorization

import functools,time,os
from flaskr.db import get_db
from flask import(
    Blueprint, 
    g, 
    redirect, 
    render_template, 
    request, 
    session, 
    url_for,
    current_app
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
                os.mkdir(current_app.config['USERFILE_DIR'] + "/" + userName)
                os.mkdir(current_app.config['USERFILE_DIR'] + "/" + userName + "/Images")
                os.system("cp flaskr/static/img/default_avatar.jpg " + current_app.config['USERFILE_DIR'] + "/" + userName + "/avatar.jpg")
                return redirect(url_for('LoginPage'))
            except db.IntegrityError:
                return "User has already existed. <a href='/login_and_register'>Back</a>"
        else:
            return "Passwords are different. <a href='/login_and_register'>Back</a>"

@bp.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        userName = request.form['username']
        passWord = request.form['password']
        db = get_db()
        users = db.execute(
            'SELECT * FROM USERS WHERE UserName = ?',(userName,)
        ).fetchone()
        if users is None:
            return "User doesn't exist. <a href='/login_and_register'>Back</a>"
        elif passWord != users['PassWord']:
            return "Incorrect password. <a href='/login_and_register'>Back</a>"
        else:
            session.clear()
            session['username'] = userName
            return redirect(url_for('index'))
        
@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))

@bp.route("/avatar", methods=('POST','GET'))
def avatar():
    if request.method == "POST":
        f = request.files['file']
        if f.filename == '':
            return redirect(url_for('profile'))
        else:
            f.save(os.path.join(current_app.config['USERFILE_DIR'],session['username'] + "/avatar.jpg"))

        return redirect(url_for('profile'))
