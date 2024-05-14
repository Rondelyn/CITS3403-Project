
from flask_bcrypt import Bcrypt
from app import db, bcrypt
from app.model import user



class UserCreationError(Exception):
    pass


def registration(idcheck, username, password):
    
    if idcheck:
        message = "user id: " +  username + " already exists" 
        raise UserCreationError(message)
        
    else:
        print("submited new user")
        hashed_password = bcrypt.generate_password_hash(password)
        new_user = user(id=username, user_password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
