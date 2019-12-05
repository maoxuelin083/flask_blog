from Blog.collect_views import col
from Blog.views import ho
from User.login_views import my, log, de
from User.register_views import reg
from User.views import bp
from common.send_email import sm


def init_route(app):
    app.register_blueprint(blueprint=bp)
    app.register_blueprint(blueprint=reg)
    app.register_blueprint(blueprint=log)
    app.register_blueprint(blueprint=my)
    app.register_blueprint(blueprint=de)
    app.register_blueprint(blueprint=ho)
    app.register_blueprint(blueprint=col)
    app.register_blueprint(blueprint=sm)