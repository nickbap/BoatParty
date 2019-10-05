from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_pagedown import PageDown
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
Bootstrap(app)
pagedown = PageDown(app)

from boatparty import routes