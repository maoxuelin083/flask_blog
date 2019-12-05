from FlaskProject.extendsions import db
from common.BaseModel import BaseModelPrimaryKey


class BlogModels(BaseModelPrimaryKey):
    title = db.Column(db.String(32), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey("user_models.id"), nullable=False)
