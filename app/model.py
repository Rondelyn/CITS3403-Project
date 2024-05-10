
from typing import List

from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#table with post data
class image(db.Model):
    image_url = db.Column(db.String, nullable=False, primary_key=True) #dont want images with the same link name
    image_catagroy = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String(10), db.ForeignKey('user.id'), nullable=False)
    image_id = db.Column(db.Integer, primary_key=True)
    image_likes = db.Column(db.Integer)
    title = db.Column(db.String)

    

    def __repr__(self) -> str:
        return f'<image {self.user_id} {self.image_url} {self.image_catagroy} {self.image_likes} >'

    


#table with user data
class user(db.Model,UserMixin):
    id = db.Column(db.String(10), primary_key=True, nullable = False, unique = True )
    #id = db.Column(db.String(20),nullable = False, unique = True)
    user_password = db.Column(db.String (80), nullable=False)

    def __repr__(self) -> str:
        return f'<image {self.user_id} {self.user_password}>' 


    def is_authenticated(self):
        return self.authenticated

#gets info from user 
class RegisterForm(FlaskForm):
    id = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    #id = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "id"})

    user_password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')


    #checks if there are any id that are the same 
    def validate_id(self, id):
        existing_user_id = user.query.filter_by(
            id=id.data).first()
        if existing_user_id:
            raise ValidationError(
                'That Username already exists. Please choose a different one.')



class LoginForm(FlaskForm):
    id = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    user_password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')

    def is_authenticated(self):
        return self.authenticated

#gets info from user 
class RegisterForm(FlaskForm):
    id = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    #id = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "id"})

    user_password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')


    #checks if there are any id that are the same 
    def validate_id(self, id):
        existing_user_id = user.query.filter_by(
            id=id.data).first()
        if existing_user_id:
            raise ValidationError(
                'That Username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    id = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    user_password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')

