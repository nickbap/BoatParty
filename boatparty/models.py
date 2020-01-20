from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from boatparty import db, login_manager


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class GuestBookPost(db.Model):
    __tablename__ = 'guest_book_posts'
    id = db.Column(db.Integer, primary_key=True)
    posted_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(80), unique=True, nullable=False)
    post_md = db.Column(db.Text, nullable=False)
    post_html = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<GuestBookPosts {} {} {}>'.format(self.id, self.posted_at, self.name)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return '<Users {} {}>'.format(self.id, self.username)
