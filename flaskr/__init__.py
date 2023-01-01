# TinyGalley
# By WeepingDogel
#

import os
import time
from . import db
from . import auth
from flask import *

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = '600c84ec0e84b99d468eafa2fdd52e1b659c9fa5e23a0ec91bab6b7e94272da8',
        DATABASE = os.path.join(app.instance_path, 'database.sqlite'),
        USERFILE_DIR = "flaskr/static/img/users",
        PUBLIC_USERFILES = "static/img/users"
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
        if 'username' in session:
            return render_template("index.html", PageTitle="HomePage", userAvaterImage=app.config['PUBLIC_USERFILES'] + "/" + session['username'] + "/avatar.jpg", userName=session['username'], logIN_Display="none" ,logOUT_Display="block", profileDisplay="block", upload="block", favorites="block")
        else:    
            return render_template("index.html", PageTitle="HomePage", userAvaterImage="static/img/default_avatar.jpg", userName="Please Log In", logIN_Display="block" ,logOUT_Display="none", profileDisplay="none", upload="none", favorites="none")
    
    @app.route("/login_and_register")
    def LoginPage():
        return render_template("auth.html", PageTitle="Sign Up or Sign In.")
    
    @app.route("/profile")
    def profile():
        if 'username' in session:
            return render_template("profile.html", userName=session['username'], AvatarLink=app.config['PUBLIC_USERFILES'] + "/" + session['username'] + "/avatar.jpg", BG_Link="static/img/defaultBG.jpg")
        else:
            return render_template("profile.html", userName="Undefined")

    db.init_app(app)
    app.register_blueprint(auth.bp)

    return app