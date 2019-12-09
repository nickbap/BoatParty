import os
import markdown2

from datetime import datetime
from flask_mail import Message
from boatparty import mail
from flask import render_template, current_app


def convert_markdown_to_html(markdown_str):
    """Converts a markdown string to an html string"""
    return markdown2.markdown(markdown_str)


def send_new_post_email(name, post):
    """Sends email notification when a Guest Book Post is made"""
    msg = Message(subject='New Guest Book Post from {}'.format(name),
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[current_app.config['SITE_ADMIN']])
    msg.html = render_template('email_notification.html', name=name, post=post)

    mail.send(msg)


def get_countdown_data():
    """Creates dict of current and wedding datetimes to pass to template"""
    now = datetime.utcnow()
    wedding_day = datetime(2020, 8, 1, 16, 0, 0)
    return {
        'now': now,
        'wedding_day': wedding_day
    }
