from flask import render_template, url_for, redirect, flash, Blueprint, current_app
from flask_mail import Message
from boatparty import db
from boatparty.forms import GuestBookForm, FAQForm
from boatparty.models import GuestBookPost
from boatparty.utils import convert_markdown_to_html, send_email_notication, get_countdown_data, get_gallery_photos

import os

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def index():
    """Home View"""
    title = 'Home'

    data = get_countdown_data()
    return render_template('home.html', title=title, **data)


@main.route('/photos')
def photos():
    """Photos View"""
    title = 'Photos'

    gallery = get_gallery_photos()
    return render_template('photos.html', title=title, gallery=gallery)


@main.route('/the-big-day')
def the_big_day():
    """The Big Day View"""
    title = 'The Big Day'
    return render_template('the-big-day.html', title=title)


@main.route('/registry')
def registry():
    """Registry View"""
    title = 'Registry'
    return render_template('registry.html', title=title)


@main.route('/guest-book', methods=['GET', 'POST'])
def guest_book():
    """Guest Book View"""
    form = GuestBookForm()
    title = 'Guest Book'

    posts = GuestBookPost.query.order_by(GuestBookPost.posted_at.desc()).all()
    if form.validate_on_submit():
        name = form.name.data
        post_md = form.pagedown.data
        post_html = convert_markdown_to_html(form.pagedown.data)

        post = GuestBookPost(name=name, post_md=post_md, post_html=post_html)

        db.session.add(post)
        db.session.commit()

        send_email_notication(name, post_html, 'guest book post')

        flash('Thanks for leaving us a note!')
        return redirect(url_for('main.guest_book'))
    return render_template('guest-book.html', title=title, form=form, posts=posts)


@main.route('/where-to-stay')
def where_to_stay():
    """Where to Stay View"""
    title = 'Where to Stay'
    return render_template('where-to-stay.html', title=title)


@main.route('/faq', methods=['GET', 'POST'])
def faq():
    """FAQ View"""
    title = 'Frequently Asked Questions'
    form = FAQForm()

    if form.validate_on_submit():
        name = form.name.data
        message = form.question.data

        send_email_notication(name, message, 'question')

        flash("Thanks for the note! We'll take a look and send you an update as soon as we can!")
        return redirect(url_for('main.faq'))
    return render_template('faq.html', title=title, form=form)


@main.route('/base')
def base_test():
    """Temporary route for checking the base template."""
    return render_template('base.html')
