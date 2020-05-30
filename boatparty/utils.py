import os
import markdown2

from datetime import datetime
from flask import render_template, current_app
from flask_mail import Message
from boatparty import mail


def convert_markdown_to_html(markdown_str):
    """Converts a markdown string to an html string"""
    return markdown2.markdown(markdown_str)


def send_email_notification(name, message, notification_type):
    """Sends email notification when a Guest Book Post or Question is made"""
    if notification_type not in {'guest book post', 'question'}:
        raise ValueError('Invalid notification type.')

    subject = 'New {notification_type} from {name}'.format(
        notification_type=notification_type.title(), name=name.title())

    msg = Message(subject=subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[current_app.config['SITE_ADMIN']])
    msg.html = render_template(
        'email-notification.html', name=name.title(), notification_type=notification_type.title(), message=message)

    mail.send(msg)


def get_countdown_data():
    """Creates dict of current and wedding datetimes to pass to template"""
    now = datetime.utcnow()
    original_wedding_day = datetime(2020, 8, 1, 16, 0, 0)
    new_wedding_day = datetime(2021, 8, 28, 16, 0, 0)
    return {
        'now': now,
        'original_wedding_day': original_wedding_day,
        'new_wedding_day': new_wedding_day
    }


def get_gallery_photos():
    """Get file names for photos in static/img/gallery"""
    gallery_dir = os.path.join(current_app.root_path, 'static/img/gallery')
    return [g for g in sorted(os.listdir(gallery_dir)) if '.jpg' in g]
