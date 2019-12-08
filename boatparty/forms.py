from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_pagedown.fields import PageDownField


class GuestBookForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    pagedown = PageDownField('Please leave us a note!\n Markdown supported!')
    submit = SubmitField('Good to Go!')
