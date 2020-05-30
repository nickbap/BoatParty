from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Email
from flask_pagedown.fields import PageDownField
from boatparty.models import GuestBookPost


class GuestBookForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    pagedown = PageDownField('Please leave us a note!\n Markdown supported!')
    recaptcha = RecaptchaField()
    submit = SubmitField('Good to Go!')

    def validate_name(self, name):
        name = GuestBookPost.query.filter_by(name=name.data).first()
        if name:
            raise ValidationError(
                "Looks like you've left us a note already! Let's save some space for others!")


class FAQForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    question = StringField('Your Question', validators=[DataRequired()])
    send = SubmitField('Send')


class AdminForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Passord', validators=[DataRequired()])
    login = SubmitField('Login')
