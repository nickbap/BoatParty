import os
import markdown2

from flask_mail import Message
from boatparty import app, mail


def convert_markdown_to_html(markdown_str):
    """Converts a markdown string to an html string"""
    return markdown2.markdown(markdown_str)


def send_new_post_email(name, post):
    """Sends email notification when a Guest Book Post is made"""
    msg = Message(subject='New Guest Book Post from {}'.format(name),
                  sender=app.config['MAIL_USERNAME'],
                  recipients=[app.config['SITE_ADMIN']])
    msg.html = post

    mail.send(msg)
