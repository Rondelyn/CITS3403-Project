
from typing import List

from flask_login import UserMixin
from app import db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError


#table with post data
class image(db.Model):
    image_url = db.Column(db.String, nullable=False)
    image_catagroy = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String(10), db.ForeignKey('user.user_id'), nullable=False)
    image_id = db.Column(db.Integer, primary_key=True)
    image_likes = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f'<image {self.user_id} {self.image_id}{self.image_catagroy}>'

#table with user data
class user(db.Model,UserMixin):
    user_id = db.Column(db.String(10), primary_key=True)
    username = db.Column(db.String(20),nullable = False, unique = True)
    user_password = db.Column(db.String (80), nullable=False)

    images = db.relationship(image)

#gets info from user 
class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    user_password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')


    #checks if there are any username that are the same 
    def validate_username(self, username):
        existing_user_username = user.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    user_password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')
