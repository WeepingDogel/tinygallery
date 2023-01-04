# Full Image Viewing And Remarking.

import uuid
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
            'SELECT FileName,ImageTitle FROM IMAGES WHERE UUID = ?;',
            (IMAGE_UUID,)
        ).fetchone()
    if 'username' in session:
        userAvaterImage = current_app.config['PUBLIC_USERFILES'] + '/' + session['username'] + '/avatar.jpg'
        return render_template(
            "remark.html", 
            PageTitle=Data['ImageTitle'], 
            FileName=Data['FileName'],
            userAvaterImage=userAvaterImage,
            userName=session['username'])
    else:
        return render_template(
            "remark.html", 
            PageTitle=Data['ImageTitle'], 
            FileName=Data['FileName'])