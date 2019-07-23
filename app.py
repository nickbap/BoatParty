from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_pagedown import PageDown
from flask_pagedown.fields import PageDownField
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from utils import convert_markdown_to_html

app = Flask(__name__)

app.config['SECRET_KEY'] = 'I_Solemnly_Swear_Im_Up_To_No_Good'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///boat_party.db'

Bootstrap(app)
pagedown = PageDown(app)
db = SQLAlchemy(app)


class GuestBookForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    pagedown = PageDownField('Please leave us a note!\n Markdown supported!')
    submit = SubmitField('Post')


class GuestBookPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    posted_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(80), unique=True, nullable=False)
    post_md = db.Column(db.Text, unique=True, nullable=False)
    post_html = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self):
        return '<GuestBookPosts {} {} {}>'.format(self.id, self.posted_at, self.name)


@app.route('/')
@app.route('/home')
def index():
    """Home View"""
    title = 'Home'
    return render_template('home.html', title=title)


@app.route('/about')
def about():
    """About Us View"""
    title = 'About Us'
    return render_template('about.html', title=title)


@app.route('/details')
def details():
    """Details View"""
    title = 'Details'
    return render_template('details.html', title=title)


@app.route('/registry')
def registry():
    """Registry View"""
    title = 'registry'
    return render_template('registry.html', title=title)


@app.route('/guest-book', methods=['GET', 'POST'])
def guest_book():
    """Guest Book View"""
    form = GuestBookForm()
    title = 'Guest Book'

    posts = GuestBookPost.query.all()
    if form.validate_on_submit():
        name = form.name.data
        post_md = form.pagedown.data
        post_html = convert_markdown_to_html(form.pagedown.data)

        post = GuestBookPost(name=name, post_md=post_md, post_html=post_html)

        db.session.add(post)
        db.session.commit()

        return redirect(url_for('guest_book'))
    return render_template('guest_book.html', title=title, form=form, posts=posts)


@app.route('/rsvp')
def rsvp():
    """RSVP View"""
    title = 'RSVP'
    return render_template('rsvp.html', title=title)


@app.route('/base')
def base_test():
    """Temporary route for checking the base template."""
    return render_template('base.html')


if __name__ == "__main__":
    app.run(debug=True)
