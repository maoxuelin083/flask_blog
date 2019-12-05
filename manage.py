

from flask_migrate import MigrateCommand
from flask_script import Manager

from FlaskProject import create_app

app = create_app()
app.config['SECRET_KEY'] = "sdadasldkakdiqwoojd"

# app.config['MAIL_SERVER'] = 'smtp.163.com'
# app.config['MAIL_PORT'] = '465'
# app.config['MAIL_USERNAME'] = 'mxl222mxl@163.com'
# app.config['MAIL_PASSWORD'] = 'Mxl960823'  # 授权码
manager = Manager(app)
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()
