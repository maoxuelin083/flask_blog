from flask_caching import Cache
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
cache = Cache()
mail = Mail()


def init_extendsions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    cache.init_app(app, config={
        "CACHE_TYPE":  "redis",
        "CACHE_REDIS_URL": "redis://:123456@localhost:6379/2"
    })
