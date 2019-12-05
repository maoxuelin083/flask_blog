from werkzeug.security import generate_password_hash, check_password_hash

from FlaskProject.extendsions import db
from common.BaseModel import BaseModelPrimaryKey


class UserModels(BaseModelPrimaryKey):
    username = db.Column(db.String(32), nullable=False, unique=True)
    _password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(32), nullable=False)
    permission = db.Column(db.Integer, default=0)   # 设置权限，默认没有权限     当发送邮件之后就有一个权限改为1

    @property
    def password(self):
        raise Exception("Can't Access")

    @password.setter
    def password(self, pwd):
        self._password = generate_password_hash(pwd)

    def verify_password(self, pwd):
        return check_password_hash(self._password, pwd)



