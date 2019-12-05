from flask import Blueprint, request, render_template, session

from FlaskProject.extendsions import cache
from common.tokens import token
from .collect_models import CollectModels
from User.models import UserModels
from .models import BlogModels

ho = Blueprint("ho", __name__)

# 这个应该是主界面
# 判断有没有用户登陆，没有则跳转到用户登陆的页面
@ho.route('/check/', methods=["POST", "GET"])
def check():
    if request.method == "GET":
        return render_template("home.html")
    elif request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        blog = BlogModels()
        # username = session.get("username")
        id = cache.get(token)
        user = UserModels.query.filter_by(id=id).first()
        if not user:
            raise Exception("没有用户")
        if title == "" or content == "":
            raise Exception("输入内容不能为空")
        blog.title = title
        blog.content = content
        blog.id_user = user.id
        if not blog.save():
            raise Exception("保存异常")
        blogs = BlogModels.query.all()
        print(blogs)
        return render_template("home.html", blogs=blogs, username=user.username)






