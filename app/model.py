
from typing import List
from app import db

class image(db.Model):
    image_url = db.Column(db.String, nullable=False)
    image_catagroy = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String(10), db.ForeignKey('user.user_id'), nullable=False)
    image_id = db.Column(db.Integer, primary_key=True)
    image_likes = db.Column(db.Integer)

class user(db.Model):
    user_id = db.Column(db.String(10), primary_key=True)
    user_password = db.Column(db.String (10), nullable=False)

