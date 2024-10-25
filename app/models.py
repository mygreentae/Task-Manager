from . import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(150), nullable=False, unique=False)
    lastname = db.Column(db.String(150), nullable=False, unique=False)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    tasks = db.relationship('Task', backref='author', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    deadline = db.Column(db.DateTime, nullable=True)
    priority = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.String(500), nullable=True)
    
    # Foreign key linking Task to User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
