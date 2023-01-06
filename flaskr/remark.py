# Full Image Viewing And Remarking.

import uuid,time
from flaskr.db import get_db
from flask import(
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for,
    current_app
)

bp = Blueprint('remark', __name__, url_prefix='/remark')

@bp.route('/<IMAGE_UUID>')
def ViewFullImage(IMAGE_UUID):
    if IMAGE_UUID != '':
        db = get_db()
        Data = db.execute(
            'SELECT OriginalFileName,ImageTitle,Description,User,Date,Dots FROM IMAGES WHERE UUID = ?;',
            (IMAGE_UUID,)
        ).fetchone()
        Comments = db.execute(
            "SELECT * FROM COMMENTS WHERE postUUID = ? Order By Date DESC",
            (IMAGE_UUID,)
            )

    if 'username' in session:
        userAvaterImage = current_app.config['PUBLIC_USERFILES'] + '/' + session['username'] + '/avatar.jpg'
        return render_template(
            "remark.html", 
            PageTitle=Data['ImageTitle'],
            ImageTitle=Data['ImageTitle'],
            Description=Data['Description'],
            Date = Data['Date'],
            User = Data['User'],
            Likes = Data['Dots'], 
            FileName=Data['OriginalFileName'],
            userAvaterImage=userAvaterImage,
            userName=session['username'],
            postUUID=IMAGE_UUID,
            Comments=Comments)
    else:
        return render_template(
            "remark.html", 
            PageTitle=Data['ImageTitle'],
            ImageTitle=Data['ImageTitle'],
            Description=Data['Description'],
            Date = Data['Date'],
            User = Data['User'],
            Likes = Data['Dots'],  
            FileName=Data['OriginalFileName'],
            postUUID=IMAGE_UUID,
            Comments=Comments)

@bp.route("/comment", methods=('POST','GET'))
def SendComment():
    if request.method == 'POST':
        db = get_db()
        User = session['username']
        postUUID = request.form['postUUID']
        ReplyTo = request.form['ReplyTo']
        ReplyToUser = request.form['ReplyToUser'] + " | " + request.form['ReplyToDate']
        Content = request.form['ContentOfComments']
        remarkUUID = str(uuid.uuid4())
        Date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if Content == "":
            return redirect(url_for("remark.ViewFullImage", IMAGE_UUID=postUUID))
        else:
            db.execute(
                "INSERT INTO COMMENTS(postUUID, remarkUUID, ReplyTo, ReplyToUser,User, Comment, Date) VALUES(?,?,?,?,?,?,?)",
                (postUUID, remarkUUID, ReplyTo, ReplyToUser, User, Content, Date))
            db.commit()
            return redirect(url_for("remark.ViewFullImage", IMAGE_UUID=postUUID))
            