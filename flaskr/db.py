# Initialize The DATABASE
# Read and Write the DATABASE

import sqlite3
import click
from flask import *

def StablizeDATABASE(name, sql):
    database = sqlite3.connect(name)
    database.execute(sql)
    database.commit()
    database.close()


@click.command("init-db")
def init_db_command():
    with open("createDATA.sql") as sqlFile:
        StablizeDATABASE("database.db", sqlFile.read())
        click.echo("DATABASE INITIALIZED!")

bp = Blueprint('db', __name__, "/")

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)