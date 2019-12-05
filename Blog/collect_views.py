from flask import Blueprint, request, session, render_template, url_for

from Blog.collect_models import CollectModels
from Blog.models import BlogModels
from FlaskProject.extendsions import cache
from User.models import UserModels
from common.tokens import token

col = Blueprint("col", __name__)


@col.route('/collect/', methods=["POST"])
def collect():
    if not request.method == "POST":
        raise Exception("请求出错")
    id = request.form.get("id")
    blog = BlogModels.query.filter_by(id=id).first()  # 找到该博客对象
    collect = CollectModels()
    collect.id_blog = blog.id
    collect.id_user = blog.id_user
    if not collect.save():
        raise Exception("收藏异常")
    id = cache.get(token)
    user = UserModels.query.filter_by(id=id).first()
    collects = CollectModels.query.filter_by(id_user=id).all()
    for collect in collects:
        user_id = collect.id_user
        blog_id = collect.id_blog
        print(user_id)
        print(blog_id)
    return render_template('collect.html', username=user.username, collects=collects)

