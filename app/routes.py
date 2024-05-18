from flask import render_template, redirect, request, url_for, flash
from app import db, login_manager
from app.controllers import *
from app.model import image, user
from app.forms import *
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from app.blueprints import main

#requred for the image upload
import os
import uuid
from flask import Flask
app = Flask(__name__)


@login_manager.user_loader
def load_user(user_id):
    return user.query.get((user_id))



#createing server connection to web pages so that you can click though them 
#landing page
@main.route("/")    
@main.route("/landingPg")
def home():
    top_images = image.query.order_by(image.image_likes.desc()).limit(5).all()
    return render_template("landingPg.html", top_images=top_images)



#createResquest/ create posts
@main.route("/createRequest")
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
@main.route('/submit', methods=['POST', 'GET'])
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

        try:
            added_image_db(image_file, categories, title, user_id)

        except NewPostError as e:
            flash(str(e), 'error')
            return redirect(location=url_for("main.images"))  
    else:
        print("Form validation errors:", form.errors)  # Debug print
    return redirect(location=url_for("main.posts"))        
  

## feed page
@main.route("/findRequest" , methods=['GET','POST'])
def posts(): 
    if not current_user.is_authenticated:
        return redirect("/login")
    formpost = postform()
    formfiter = catergoryFilter() 
    formreport = deleate()
    posts = image.query.all()

    return render_template("findRequest.html", images=posts, form = formpost, formfilter = formfiter, formreport=formreport)

#submits filter on feed page 
@main.route('/submitfilter', methods = ["post", "get"])
def submitfilter():
    formpost = postform()
    formfilter = catergoryFilter()
    formreport = deleate() 
    
    if  formfilter.validate_on_submit():
        filterSelected = formfilter.filter.data
        posts =image.query.filter(image.image_catagroy.contains(filterSelected))      
        return render_template("findRequest.html", images=posts, form=formpost, formfilter = formfilter, formreport=formreport)
    
    else:
        posts = image.query.all()
        return redirect(location=url_for("main.posts"))
    
  
    
##adds star rating to db
@main.route("/submitstar/<post>", methods = ["post", "get"])
def addstarvalue(post):
    ## only works when button is clicked 
    form = postform()
    rating = int(form.starvalue.data)
    post_id = post
    if form.validate_on_submit():
            row = image.query.get(post_id)
            row.image_likes += rating
            db.session.commit()
    return redirect(location=url_for("main.posts"))

##deleates reported post 
@main.route("/report/<post>", methods = ["post", "get"])
def report(post):
    post_id = post
    formreport = deleate()  

    if not formreport.validate_on_submit():
        return redirect(location=url_for("main.posts"))

    #If vaild will check its a vaild reason
    resongiven = formreport.reason.data
    try:
        reporting_post(post_id, resongiven)
        flash('Thankyou for reporting :)', 'error')

    except FeedpageUseError as e:
        flash(str(e), 'error')
        return redirect(location=url_for("main.posts"))

    return redirect(location=url_for("main.posts"))



#login page
@main.route("/login", methods=['GET','POST'])
def loginform():
    form = LoginForm()
    #On a GET request or if for not validate on submite renders login page 
    if request.method == "GET" or not form.validate_on_submit():
        return render_template('login.html', form=form)


    #trys to login user, if it fails returns to login page else to the post page
    try:
        the_user = login_the_user(form.id.data, form.user_password.data)

    except UserCreationError as e:
        flash(str(e), 'error')
        return redirect(location=url_for("main.loginform"))
    
    login_user(the_user)    
    return redirect(location=url_for("main.posts"))


@main.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(location=url_for("main.loginform"))


#register page
@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    #for get request and if form is not validate on submite renders register page
    if request.method == "GET" or not form.validate_on_submit():
        return render_template('register.html', form=form)
    
    #for POST request, trys to register user. If fails, sends them to register page else to the post page
    
    try:
        newuser = registration(form.id.data, form.user_password.data)

    except UserCreationError as e:
        flash(str(e), 'error')
        return redirect('register')
    
    login_user(newuser)  
    return redirect(location=url_for("main.posts"))
    