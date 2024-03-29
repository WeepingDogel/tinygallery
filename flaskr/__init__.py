# TinyGalley
# By WeepingDogel
#

import os
import time
from . import db
from . import auth
from . import remark
from . import action
from flask import *


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='600c84ec0e84b99d468eafa2fdd52e1b659c9fa5e23a0ec91bab6b7e94272da8',
        DATABASE=os.path.join(app.instance_path, 'database.sqlite'),
        USERFILE_DIR="flaskr/static/img/users",
        PUBLIC_USERFILES="/static/img/users"
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    if os.path.exists(app.config['USERFILE_DIR']) == False:
        os.mkdir(app.config['USERFILE_DIR'])

    @app.route("/")
    def index():
        database = db.get_db()
        ImageTable = database.execute(
            "SELECT * FROM IMAGES ORDER BY Date DESC")
        if 'username' in session:
            LikeTable = database.execute(
                "SELECT LikedPostUUID FROM ImagesLikedByUser WHERE User = ? AND LikeStatus = ?",
                (session['username'], 1,)).fetchall()
            LikedList = []
            for i in LikeTable:
                LikedList.append(str(i[0]))
            Avatar = database.execute(
                'SELECT Avatar FROM AVATARS WHERE UserName = ?',
                (session['username'],)
            ).fetchone()
            userAvaterImage = app.config['PUBLIC_USERFILES'] + \
                '/' + session['username'] + '/' + Avatar['Avatar']
            return render_template(
                "index.html",
                PageTitle="HomePage",
                Images=ImageTable,
                userAvaterImage=userAvaterImage,
                userName=session['username'],
                LikedList=LikedList)
        else:
            return render_template(
                "index.html",
                PageTitle="HomePage",
                Images=ImageTable)

    @app.route("/login_and_register")
    def LoginPage():
        return render_template("auth.html", PageTitle="Sign Up or Sign In.")

    @app.route("/profile")
    def profile():
        database = db.get_db()
        if 'username' in session:
            Avatar = database.execute(
                'SELECT Avatar FROM AVATARS WHERE UserName = ?',
                (session['username'],)).fetchone()
            LikeTable = database.execute(
                "SELECT LikedPostUUID FROM ImagesLikedByUser WHERE User = ? AND LikeStatus = ?",
                (session['username'], 1,)).fetchall()
            LikedList = []
            for i in LikeTable:
                LikedList.append(str(i[0]))
            ImageTable = database.execute(
                "SELECT * FROM IMAGES WHERE User = ?", (session['username'],))
            return render_template(
                "profile.html",
                userName=session['username'],
                AvatarLink=app.config['PUBLIC_USERFILES'] + "/" +
                session['username'] + "/" + Avatar['Avatar'],
                BG_Link="static/img/defaultBG.jpg",
                Images=ImageTable,
                LikedList=LikedList)
        else:
            return render_template("profile.html", userName="Undefined")

    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(remark.bp)
    app.register_blueprint(action.bp)

    return app
