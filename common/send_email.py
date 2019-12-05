
from flask import Blueprint
from flask_mail import Message

from FlaskProject.extendsions import mail

sm = Blueprint("sm", __name__)


@sm.route('/send/')
def send():
    # if request.method == "POST":
    content = "<h1>人总是对未知充满恐惧</h1>"

    msg = Message("Hello", sender="mxl222mxl@163.com", recipients=["529837812@qq.com", ], html=content)

    mail.send(msg)

    return "successful"








