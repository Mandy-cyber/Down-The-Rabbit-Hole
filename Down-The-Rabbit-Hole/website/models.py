from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(16))
    snippets = db.relationship('Snippet')

class Snippet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    snipText = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))