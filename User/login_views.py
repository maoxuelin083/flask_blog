

from flask import Blueprint, request, render_template, session, url_for, redirect

from FlaskProject.extendsions import db, cache
from User.models import UserModels
from common.tokens import token, TIMEOUT

log = Blueprint("log", __name__)
my = Blueprint("my", __name__)
de = Blueprint("de", __name__)


@log.route('/login/', methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = UserModels.query.filter_by(username=username).first()
        if not user.verify_password(password):
            raise Exception("密码输入有误")
        # session['username'] = username
        cache.set(token, user.id, TIMEOUT)   # 设置过期时间
        return redirect(url_for("my.home"))


@my.route('/home/')
def home():
    # username = session.get("username")
    id = cache.get(token)
    # user = UserModels.query.filter_by(username=username).first()
    user = UserModels.query.filter_by(id=id).first()
    if not user:
        raise Exception("账号有误")
    return render_template("home.html", username=user.username)


@de.route("/delete/", methods=["GET"])
def delete():
    if request.method == "GET":
        # del session["username"]
        cache.delete(token)
        return render_template("login.html")
    else:
        raise Exception("出错")
