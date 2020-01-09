from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from boatparty import db


class GuestBookPost(db.Model):
    __tablename__ = 'guest_book_posts'
    id = db.Column(db.Integer, primary_key=True)
    posted_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(80), unique=True, nullable=False)
    post_md = db.Column(db.Text, nullable=False)
    post_html = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<GuestBookPosts {} {} {}>'.format(self.id, self.posted_at, self.name)
