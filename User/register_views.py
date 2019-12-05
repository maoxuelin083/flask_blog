from flask import Blueprint, request, render_template, session

from User.models import UserModels

reg = Blueprint("reg", __name__)


@reg.route('/register/', methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        user = UserModels()
        user.username = username
        user.password = password
        user.email = email
        if not user.save():
            raise Exception("输入不正确")
        return render_template("login.html")





