# Authorization

import functools,time,os,uuid,cv2
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
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp'}

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
                db.execute("INSERT INTO USERS(UserName, PassWord, Email, Date) VALUES(?, ?, ?, ?)",
                    (userName, passWord, Email, Date))
                db.commit()
                os.mkdir(current_app.config['USERFILE_DIR'] + "/" + userName)
                os.mkdir(current_app.config['USERFILE_DIR'] + "/" + userName + "/Images")
                os.mkdir(current_app.config['USERFILE_DIR'] + "/" + userName + "/Images/Original")
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

@bp.route("/upload", methods=('POST','GET'))
def upload():
    
    def allowed_file(filename):
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    if request.method == "POST":
        UploadLoacation = os.path.join(current_app.config['USERFILE_DIR'],session['username'] + "/Images/Original")
        db = get_db()
        f = request.files['Picture']
        if f.filename == '':
            return "Empty file is not allowed to submit <a href='/'>Back</a>"
        elif allowed_file(f.filename):
            OriginalFileName = current_app.config['PUBLIC_USERFILES'] + "/" + session['username'] + "/Images" + "/Original/" + f.filename
            ImageTitle = request.form['Title']
            Description = request.form['Description']
            User = session['username']
            Date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            UUID = str(uuid.uuid4())
            db.execute(
                "INSERT INTO IMAGES(UUID, OriginalFileName, ImageTitle, Description, User, Date) VALUES(?, ?, ?, ?, ?, ?)",
                (UUID , OriginalFileName, ImageTitle, Description, User, Date))
            db.commit()
            f.save(UploadLoacation + "/" + f.filename)
            img = cv2.imread(UploadLoacation + "/" + f.filename)
            h,w = img.shape[:2]
            new_h, new_w = int(h / 3),int(w / 3)
            resizedImg = cv2.resize(img, (new_w, new_h))
            cv2.imwrite(current_app.config['USERFILE_DIR'] + "/" + session['username'] + "/Images/" + UUID + ".jpg" , resizedImg)
            return redirect(url_for('index'))
        else:
            return "Invalid Filename " + f.filename + " <a href='/'>Back</a>"

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('username')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM USERS WHERE UserName = ?', (user_id,)
        ).fetchone()
        