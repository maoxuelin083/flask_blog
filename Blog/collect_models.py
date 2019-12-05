from FlaskProject.extendsions import db
from common.BaseModel import BaseModelPrimaryKey


class CollectModels(BaseModelPrimaryKey):
    id_blog = db.Column(db.Integer, db.ForeignKey("blog_models.id"))
    id_user = db.Column(db.Integer, db.ForeignKey("user_models.id"))




