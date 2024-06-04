from web import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    second_name = db.Column(db.String(150), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
