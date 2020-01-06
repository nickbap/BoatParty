from flask import Blueprint, render_template
from boatparty import db


error = Blueprint('error', __name__)


@error.app_errorhandler(404)
def page_not_found(error):
    """Response for 404 Not found"""
    return render_template('errors/404.html'), 404


@error.app_errorhandler(500)
def internal_error(error):
    """Reponse for 500 Internal Service Error"""
    db.session.rollback()
    return render_template('errors/500.html'), 500
