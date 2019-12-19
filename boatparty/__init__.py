from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pagedown import PageDown
from flask_mail import Mail
from flask_moment import Moment
from config import Config


db = SQLAlchemy()
pagedown = PageDown()
mail = Mail()
moment = Moment()


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    pagedown.init_app(app)
    mail.init_app(app)
    moment.init_app(app)

    from boatparty.routes import main
    app.register_blueprint(main)
    return app
