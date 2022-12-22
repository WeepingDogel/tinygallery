# TinyGalley
# By WeepingDogel
#

import os
import time
from . import db
from . import auth
from flask import *


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    @app.route("/")
    def index():
        return render_template("index.html", PageTitle="HomePage", userAvaterImage="static/avatars/test.jpg", userName="Please Log In", logIN_Display="block" ,logOUT_Display="none")
    @app.route("/login_and_register")
    def loginPage():
        return render_template("auth.html", PageTitle="Sign Up or Sign In.")
    return app