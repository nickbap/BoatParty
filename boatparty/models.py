from boatparty import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


class GuestBookPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    posted_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(80), unique=True, nullable=False)
    post_md = db.Column(db.Text, unique=True, nullable=False)
    post_html = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self):
        return '<GuestBookPosts {} {} {}>'.format(self.id, self.posted_at, self.name)
