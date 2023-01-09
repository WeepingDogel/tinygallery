from flaskr.db import get_db
from flask import(
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for,
    current_app,
    jsonify
)

bp = Blueprint('action',__name__, url_prefix="/action")

@bp.route("/likeCheck")
def likeCheck():
    if request.method == "GET":
        db = get_db()
        userName = session['username']
        postUUID = str(request.args.get("UUID")) # Get UUID value from Ajax Request by method GET.)
        LikeStatus = int(request.args.get("LikeStatus")) # Get LikeStatus value from Ajax Request by method GET.
        if postUUID == "":
            return "刷你妈呢", 403
        elif userName is None:
            return "错误：用户没登录", 403
        elif LikeStatus != 0 and LikeStatus > 1:
            return "必须是 1 和 0才能生效，你是不是利用浏览器来刷了？会没唧唧的哦！", 403
        elif LikeStatus == 1:
            LikeTable = db.execute(
                "SELECT * FROM ImagesLikedByUser WHERE User = ? and LikedPostUUID = ?",
                (userName,postUUID)).fetchone()
            if LikeTable is None:
                db.execute(
                    "INSERT INTO ImagesLikedByUser(User, LikedPostUUID, LikeStatus ) VALUES(?,?,?)",
                    (userName, postUUID, LikeStatus))
                db.commit()
                Dots = db.execute(
                    "SELECT Dots FROM IMAGES WHERE UUID=?",
                    (postUUID,)
                ).fetchone()
                newDots = int(Dots['Dots']) + 1
                db.execute(
                    "UPDATE IMAGES SET Dots = ? WHERE UUID = ?",
                    (newDots, postUUID))
                db.commit()
                DotsToReturn = db.execute(
                    "SELECT Dots FROM IMAGES WHERE UUID=?",
                    (postUUID,)).fetchone()
                LikeStatusToReturn = db.execute(
                    "SELECT LikeStatus FROM ImagesLikedByUser WHERE User = ? and LikedPostUUID = ?",
                    (userName,postUUID,)).fetchone()
                return jsonify(
                    Status = LikeStatusToReturn['LikeStatus'],
                    Dots = DotsToReturn['Dots']
                )
            else:
                if LikeTable['LikeStatus'] == 1:
                    return "已经点过了", 500
                elif LikeTable['LikeStatus'] == 0:
                    db.execute(
                        "UPDATE ImagesLikedByUser SET LikeStatus = 1 WHERE User = ? AND LikedPostUUID = ?",
                        (userName,postUUID,))
                    db.commit()
                    Dots = db.execute(
                        "SELECT Dots FROM IMAGES WHERE UUID=?",
                        (postUUID,)
                        ).fetchone()
                    newDots = int(Dots['Dots']) + 1
                    db.execute(
                        "UPDATE IMAGES SET Dots = ? WHERE UUID = ?",
                        (newDots, postUUID))
                    db.commit()
                    DotsToReturn = db.execute(
                        "SELECT Dots FROM IMAGES WHERE UUID=?",
                        (postUUID,)).fetchone()
                    LikeStatusToReturn = db.execute(
                        "SELECT LikeStatus FROM ImagesLikedByUser WHERE User = ? and LikedPostUUID = ?",
                        (userName,postUUID,)).fetchone()
                    return jsonify(
                        Status = LikeStatusToReturn['LikeStatus'],
                        Dots = DotsToReturn['Dots']
                    )
        elif LikeStatus == 0:
            LikeTable = db.execute(
                "SELECT * FROM ImagesLikedByUser WHERE User = ? and LikedPostUUID = ?",
                (userName,postUUID)).fetchone()
            if LikeTable['LikeStatus'] == 1:
                db.execute(
                    "UPDATE ImagesLikedByUser SET LikeStatus = 0 WHERE User = ? AND LikedPostUUID = ?",
                    (userName,postUUID,))
                db.commit()
                Dots = db.execute(
                    "SELECT Dots FROM IMAGES WHERE UUID=?",
                    (postUUID,)).fetchone()
                newDots = int(Dots['Dots']) - 1
                db.execute(
                    "UPDATE IMAGES SET Dots = ? WHERE UUID = ?",
                    (newDots, postUUID))
                db.commit()
                DotsToReturn = db.execute(
                    "SELECT Dots FROM IMAGES WHERE UUID=?",
                    (postUUID,)).fetchone()
                LikeStatusToReturn = db.execute(
                    "SELECT LikeStatus FROM ImagesLikedByUser WHERE User = ? and LikedPostUUID = ?",
                    (userName,postUUID,)).fetchone()
                return jsonify(
                    Status = LikeStatusToReturn['LikeStatus'],
                    Dots = DotsToReturn['Dots']
                )
            else:
                return "你已经取消过了", 500