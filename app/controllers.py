import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('RATE_MY_FIT_SECRET_KEY_12')

class DeploymentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'app.db')

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    


from flask_bcrypt import Bcrypt
from app import db, bcrypt
from app.model import image, user



class UserCreationError(Exception):
    pass

class UserExistsError(Exception):
    pass

class FeedpageUseError(Exception):
    pass
class NewPostError(Exception):
    pass


#for the signup page, registers the user
def registration(username, password):
    #checks the username dosn't already exists
    idcheck = db.session.get(user, username) 
    
    if idcheck:
        message = "user id: " +  username + " already exists" 
        raise UserCreationError(message)
    #returns the user to be logied in 
    else:
        print("submited new user")
        hashed_password = bcrypt.generate_password_hash(password)
        new_user = user(id=username, user_password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        the_user = user.query.filter_by(id=username).first()
        return the_user


##for the login page, checks user unputs
def login_the_user(username, password):
    idcheck = db.session.get(user, username) 

    #if username dossn't exist  
    if not idcheck:
        message = "user id: " +  username + " dose not exist" 
        raise UserExistsError(message)

    #checks the password is correct
    the_user = user.query.filter_by(id=username).first()
    if the_user:
        if bcrypt.check_password_hash(the_user.user_password, password):
            return the_user
        else:
            message = "password is incorrect" 
            raise UserExistsError(message)
        

##crecks a reported post if it has a vaild reason to be taken down
def reporting_post(post_id, resongiven):
    
    validreasons = ["inappropriate", "stolen", "wrong category"]

    if resongiven in validreasons:      
        user = image.query.get(post_id)
        db.session.delete(user)
        db.session.commit()
        
    else:
        message = "Not a vaild reason" 
        raise FeedpageUseError(message)
    

def added_image_db(image_file, categories, title, user_id):
        
        if image_file:
            if db.session.get(image, image_file):
                message = "Image with that name already uploaded" 
                raise NewPostError(message)

            new_image = image(image_url=image_file, image_catagroy= categories, image_likes=0, title=title, user_id=user_id)
            print("New Image Object:", new_image)  # Debug print
            db.session.add(new_image)
            db.session.commit()           
        
        else:
            message = "Failed to upload image" 
            raise NewPostError(message)

