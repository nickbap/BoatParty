from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from flask_pagedown.fields import PageDownField
from boatparty.models import GuestBookPost


class GuestBookForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    pagedown = PageDownField('Please leave us a note!\n Markdown supported!')
    submit = SubmitField('Good to Go!')

    def validate_name(self, name):
        name = GuestBookPost.query.filter_by(name=name.data).first()
        if name:
            raise ValidationError(
                "Looks like you've left us a note already! Let's save some space for others!")
