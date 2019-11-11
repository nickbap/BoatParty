from flask import render_template, url_for, redirect, flash
from flask_mail import Message
from boatparty import app, db
from boatparty.forms import GuestBookForm
from boatparty.models import GuestBookPost
from boatparty.utils import convert_markdown_to_html, send_new_post_email

import os


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

    gallery_dir = os.path.join(app.root_path, 'static/img/gallery')
    gallery = [x for x in sorted(os.listdir(gallery_dir))]
    return render_template('about.html', title=title, gallery=gallery)


@app.route('/details')
def details():
    """Details View"""
    title = 'Details'
    return render_template('details.html', title=title)


@app.route('/registry')
def registry():
    """Registry View"""
    title = 'Registry'
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

        send_new_post_email(name, post_html)

        flash('Thanks for leaving us a note!')
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
