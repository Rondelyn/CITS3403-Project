
#improting required classes
from flask import render_template, redirect, request, url_for, flash
from app import flaskApp, db
from app.model import image, user
from app.forms import Createpost, Createlogin, catergoryFilter

#requred for the image upload
import os
from flask import Flask
app = Flask(__name__)




#createing server connection to web pages so that you can click though them 
#landing page
@flaskApp.route("/")    
@flaskApp.route("/landingPg")
def home():
    top_images = image.query.order_by(image.image_likes.desc()).limit(5).all()
    return render_template("landingPg.html", top_images=top_images)

#login page
@flaskApp.route("/login")
def loginform():
    form2 = Createlogin()
    return render_template("login.html", form = form2)

#find request page/ posts
@flaskApp.route("/findRequest")
def posts():
    form = catergoryFilter()
    posts = image.query.all()
    return render_template("findRequest.html", images=posts, form = form)


    
@flaskApp.route('/submitfilter', methods = ['POST'])
def submitfilter():
    form = catergoryFilter() 
    if form.validate_on_submit():
        filterSelected = form.filter.data
        posts =image.query.filter(image.image_catagroy.contains(filterSelected))
                
        return render_template("findRequest.html", images=posts, form = form)
    
    else:
        posts = image.query.all()
        return render_template("findRequest.html", images=posts, form = form)



#createResquest/ create post
##rename images to createpost?
@flaskApp.route("/createRequest")
def images():
    form1 = Createpost()
    return render_template("createRequest.html", form = form1)


#adding submit point for posts
def save_image(picture_file):
    picture = picture_file.filename
    picture_path = os.path.join(app.root_path, 'static/image_uploads', picture)
    picture_file.save(picture_path)
    return picture

#allows users to submit there posts
@flaskApp.route('/submit', methods=['POST', 'Get'])
def submit():
    form = Createpost()
    #validation

    if form.validate_on_submit():
            
            categoriy =  ' '.join(form.categories.data)
            print(categoriy)
            image_file = save_image(form.image.data)
            comment = form.title.data
            new_image  = image(image_url= image_file, image_catagroy= categoriy, user_id="johdsn", image_likes=0, title= comment) #need to change the hard code of the user_id to the user id once logged in
            db.session.add(new_image)
            db.session.commit()
            return redirect(location=url_for("posts"))
        
    else:
        flash("You must submit an image", 'error')
    
    return render_template('createRequest.html', form=form) 



##submite form for the create new user
@flaskApp.route('/createuser',  methods=['GET', 'POST'])
def createuser():
    form = Createlogin()
    
    if form.validate_on_submit():
        return render_template('createRequest.html', form=form)

    username = str(form.username.data)
    username_exists = find_user_exists(username) #None
    
    if (username_exists): #If it exists 
        return render_template('login.html', form=form)
    
    #else it adds the perseon to  the db and sends them to the posts page 
    password = str(form.password.data)
    newuser = user(user_id=username, user_password=password)
    
    db.session.add(newuser)
    db.session.commit()
    
    return redirect(location=url_for("posts"))


##submite form for the login 
@flaskApp.route('/submitlogin',  methods=['GET', 'POST'])
def submitlogin():
    form = Createlogin()
    
    if form.validate_on_submit():
        
        return render_template('login.html', form=form)

    
    username = find_user(form.username.data)
    password = find_userpassword(form.password.data)

    if not (username):
        return render_template('login.html', form=form)

    if not (password):
        return render_template('login.html', form=form)    

    
    return redirect(location=url_for("posts"))



#check the database for the user id and password
def find_user(user_id:str):
    user1username = user.query.get(user_id)

    if not user1username:
        flash(f'Username does not exist: {user_id}', 'error')
    return user1username

def find_userpassword(user_password:str):

    user1password = user.query.get(user_password)
    if not user1password:
        flash(f'password incorrect {user_password}', 'error')
    
    return user1password


def find_user_exists(user_id:str):
    username_not_exist = user.query.get(user_id) #will ne none if db it donsn't contain that user
    
    if username_not_exist: #if user i.e "user" exists willl be called
        flash(f'Username already exists: {user_id}', 'error')
    return username_not_exist #returns a None


