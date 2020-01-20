from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_pagedown import PageDown
from flask_mail import Mail
from flask_moment import Moment
from flask_login import LoginManager
from config import Config


db = SQLAlchemy()
migrate = Migrate()
pagedown = PageDown()
mail = Mail()
moment = Moment()
login_manager = LoginManager()


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    pagedown.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)

    from boatparty.routes import main
    app.register_blueprint(main)

    from boatparty.errors import error
    app.register_blueprint(error)

    return app
