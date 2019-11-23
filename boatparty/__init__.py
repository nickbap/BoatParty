from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_pagedown import PageDown
from flask_mail import Mail
from flask_moment import Moment
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
Bootstrap(app)
pagedown = PageDown(app)
mail = Mail(app)
moment = Moment(app)

from boatparty import routes