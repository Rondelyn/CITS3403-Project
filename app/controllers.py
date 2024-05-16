from flask_bcrypt import Bcrypt
from app import db, bcrypt
from app.model import image, user

print("controlers file nnnnn")

class UserCreationError(Exception):
    pass

class UserExistsError(Exception):
    pass

class FeedpageUseError(Exception):
    pass
class NewPostError(Exception):
    pass




##for the signup page, registers the user
def registration(idcheck, username, password):
    #checks the username dosn't already exists
    if idcheck:
        message = "user id: " +  username + " already exists" 
        raise UserCreationError(message)
        
    else:
        print("submited new user")
        hashed_password = bcrypt.generate_password_hash(password)
        new_user = user(id=username, user_password=hashed_password)
        db.session.add(new_user)
        db.session.commit()


##for the login page, checks user unputs
def login_the_user(idcheck, username, password):

    #if username dossn't exist  
    if not idcheck:
        message = "user id: " +  username + " dose not exist" 
        raise UserCreationError(message)

    #checks the password is correct
    the_user = user.query.filter_by(id=username).first()
    if the_user:
        if bcrypt.check_password_hash(the_user.user_password, password):
            return the_user
        else:
            message = "password is incorrect" 
            raise UserCreationError(message)
        

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
            new_image = image(image_url=image_file, image_catagroy= categories, image_likes=0, title=title, user_id=user_id)
            print("New Image Object:", new_image)  # Debug print
            db.session.add(new_image)
            db.session.commit()
            
        
        else:
            message = "Failed to upload image" 
            raise NewPostError(message)



    

