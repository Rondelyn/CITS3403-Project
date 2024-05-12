
# required classes
from flask import render_template, redirect, request, url_for, flash
from app import flaskApp, db
from app.model import image, user
from app.forms import *
from flask_bcrypt import Bcrypt
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

#requred for the image upload
import os
import uuid
from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy



bcrypt = Bcrypt(flaskApp)

login_manager = LoginManager()
login_manager.init_app(flaskApp)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return user.query.get((user_id))



#createing server connection to web pages so that you can click though them 
#landing page
@flaskApp.route("/")    
@flaskApp.route("/landingPg")
def home():
    top_images = image.query.order_by(image.image_likes.desc()).limit(5).all()
    return render_template("landingPg.html", top_images=top_images)



#createResquest/ create posts
@flaskApp.route("/createRequest")
def images():
        if not current_user.is_authenticated:
            return redirect("/login")
        form1 = Createpost()
        return render_template("createRequest.html", form = form1)


#saves images to file location image_uploads 
def save_image(image_file):
    if image_file:
        # Generate unique filename using UUID
        unique_filename = str(uuid.uuid4()) + '_' + image_file.filename
        image_path = os.path.join(app.root_path, 'static/image_uploads', unique_filename)
        image_file.save(image_path)
        return unique_filename
    return None


#allows users to submit there posts
@flaskApp.route('/submit', methods=['POST', 'GET'])
def submit():
    print("Inside submit function")  # Debug print
    form = Createpost()
    #validation

    if form.validate_on_submit():
        print("Form data:", form.data)  # Debug print
        categories = ' '.join(form.catagories.data)
        image_file = save_image(request.files['image'])
        title = form.title.data
        user_id = current_user.id
        print("User ID:", user_id)  # Debug print

        if image_file:
            new_image = image(image_url=image_file, image_catagroy= categories, image_likes=0, title=title, user_id=user_id)
            print("New Image Object:", new_image)  # Debug print
            db.session.add(new_image)
            db.session.commit()
            return redirect(url_for("posts"))
        else:
            flash("Failed to upload image", 'error')
    else:
        print("Form validation errors:", form.errors)  # Debug print
            
    return render_template('createRequest.html', form=form)

## feed page
@flaskApp.route("/findRequest" , methods=['GET','POST'])
def posts(): 
    if not current_user.is_authenticated:
        return redirect("/login")
    formpost = postform()
    formfiter = catergoryFilter() 
    formreport = deleate()
    posts = image.query.all()

    return render_template("findRequest.html", images=posts, form = formpost, formfilter = formfiter, formreport=formreport)

#submits filter on feed page 
@flaskApp.route('/submitfilter', methods = ["post", "get"])
def submitfilter():
    formpost = postform()
    formfilter = catergoryFilter()
    formreport = deleate() 
    print(formfilter.errors)
    if  formfilter.validate_on_submit():
        
        filterSelected = formfilter.filter.data
        posts =image.query.filter(image.image_catagroy.contains(filterSelected))
                
        return render_template("findRequest.html", images=posts, form=formpost, formfilter = formfilter, formreport=formreport)
    
    else:
        posts = image.query.all()
        print("ksksk")
        return redirect(location=url_for("posts"))
    
  
    
##adds star rating to db
@flaskApp.route("/submitstar/<post>", methods = ["post", "get"])
def addstarvalue(post):
    ## only works when button is clicked 
    form = postform()
    print(form.starvalue.data)
    rating = int(form.starvalue.data)
    post_id = post
    
    rowd = image.query.filter_by(image_url = post_id)
    row = image.query.get(post_id)
    row.image_likes += rating
    print(row)
    
    db.session.commit()
    return redirect(location=url_for("posts"))

##deleates reported post 
@flaskApp.route("/report/<post>", methods = ["post", "get"])
def report(post):
    post_id = post
    formreport = deleate()
    formpost = postform()
    formfilter = catergoryFilter()
    
    
    if  formreport.validate_on_submit():
        filterSelected = formreport.reason.data
        remove = resons(filterSelected)

        if remove:
            
            user = image.query.get(post_id)
            db.session.delete(user)
            db.session.commit()
            return redirect(location=url_for("posts"))
        else:
            flash("Not a vaild reason", 'error')           
            return redirect(location=url_for("posts"))
    
    
    return redirect(location=url_for("posts"))


def resons(filterSelected):
    validreasons = ["inappropriate", "stolen", "wrong category"]
    print(filterSelected)
    if filterSelected in validreasons:
        return True
    return False




##login form 

#login page
@flaskApp.route("/login", methods=['GET','POST'])
def loginform():
    form = LoginForm()
    idcheck= user.query.get(form.id.data)


    if request.method == "GET":
        return render_template('login.html', form=form)

    if not idcheck:
        flash(f'username {form.id.data} dose not exists', 'error')
        return redirect('/login')


    if form.validate_on_submit():
        the_user = user.query.filter_by(id=form.id.data).first()
        if the_user:
            if bcrypt.check_password_hash(the_user.user_password, form.user_password.data):
                login_user(the_user)
                return redirect(('/findRequest'))


    return redirect('/login')


@flaskApp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('/login')


@ flaskApp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    formpost = postform()
    formfilter = catergoryFilter() 
    idcheck= user.query.get(form.id.data)


    if request.method == "GET":
        return render_template('register.html', form=form)

    if idcheck:
        flash(f'username {form.id.data} already exists', 'error')
        return render_template('register.html', form=form)

    if form.validate_on_submit() and not idcheck:
        hashed_password = bcrypt.generate_password_hash(form.user_password.data)
        new_user = user(id=form.id.data, user_password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(('/findRequest'))
    
    return render_template('register.html', form=form)



