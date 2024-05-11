
from typing import List

from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


#table with post data
class image(db.Model):
    image_url = db.Column(db.String, nullable=False, primary_key=True) #dont want images with the same link name
    image_catagroy = db.Column(db.String, nullable=False)
    image_likes = db.Column(db.Integer)
    title = db.Column(db.String)

    

    def __repr__(self) -> str:
        return f'<image {self.image_url} {self.image_catagroy} {self.image_likes} >'

    


#table with user data
class user(db.Model,UserMixin):
    id = db.Column(db.String(10), primary_key=True)
    user_password = db.Column(db.String (10), nullable=False)
    #password_hash = db.Column(db.String(128), nullable = False)

    def __repr__(self) -> str:
        return f'<image {self.user_id} {self.user_password}>' 


    def is_authenticated(self):
        return self.authenticated

