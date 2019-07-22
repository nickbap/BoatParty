from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_pagedown import PageDown
from flask_pagedown.fields import PageDownField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'I_Solemnly_Swear_Im_Up_To_No_Good'

Bootstrap(app)
pagedown = PageDown(app)


class GuestBook(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    pagedown = PageDownField('Please leave us a note!\n Markdown supported!')
    submit = SubmitField('Post')


@app.route('/')
@app.route('/home')
def index():
    title = 'Home'
    return render_template('home.html', title=title)


@app.route('/about')
def about():
    title = 'About Us'
    return render_template('about.html', title=title)


@app.route('/details')
def details():
    title = 'Details'
    return render_template('details.html', title=title)


@app.route('/registry')
def registry():
    title = 'registry'
    return render_template('registry.html', title=title)


@app.route('/guest-book')
def guest_book():
    form = GuestBook()
    title = 'Guest Book'
    return render_template('guest_book.html', title=title, form=form)


@app.route('/rsvp')
def rsvp():
    title = 'RSVP'
    return render_template('rsvp.html', title=title)


@app.route('/base')
def base_test():
    """Temporary route for checking the base template."""
    return render_template('base.html')


if __name__ == "__main__":
    app.run(debug=True)
