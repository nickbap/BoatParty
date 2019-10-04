from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_pagedown import PageDown

app = Flask(__name__)
app.config['SECRET_KEY'] = 'I_Solemnly_Swear_Im_Up_To_No_Good'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///boat_party.db'

db = SQLAlchemy(app)
Bootstrap(app)
pagedown = PageDown(app)

from boatparty import routes