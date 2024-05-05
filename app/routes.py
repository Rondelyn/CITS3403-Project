
#improting required classes
from flask import render_template, redirect, request, url_for, flash
from app import flaskApp
from app.model import image, user
from app.forms import Createpost, Createlogin




#createing server connection to web pages so that you can click though them 
#landing page
@flaskApp.route("/")    
@flaskApp.route("/landingPg")
def home():
    return render_template("landingPg.html")

#login page
@flaskApp.route("/login")
def loginform():
    form2 = Createlogin()
    return render_template("login.html", form = form2)

#find request page/ posts
@flaskApp.route("/findRequest")
def posts():
    posts = image.query.all()
    return render_template("findRequest.html", images=posts )



#createResquest/ create post
##rename images to createpost?
@flaskApp.route("/createRequest")
def images():
    form1 = Createpost()
    return render_template("createRequest.html", form = form1)


#adding submit point for posts

@flaskApp.route('/submit', methods=['POST'])
def submit():
    
    form = Createpost()
    print(request.form)
    if form.validate_on_submit():
        
        return render_template('createRequest.html', form=form)

    print("submitted")
    print(request.form)
    return redirect(location=url_for("posts"))

##submite form for the login 
@flaskApp.route('/submitlogin',  methods=['GET', 'POST'])
def submitlogin():
    print("fail")
    form = Createlogin()
    print("foorm")
    print(request.form)
    if form.validate_on_submit():
        print("fail1")
        return render_template('login.html', form=form)

    
    username = find_user(form.username.data)
    

    if not (username):
        print("fail2")
        return render_template('login.html', form=form)
    
    password = find_userpassword(form.password.data)

    if not (password):
        print("fail2")
        return render_template('login.html', form=form)    

    print("nope")
    return redirect(location=url_for("posts"))

##submite form for the create new user
@flaskApp.route('/createuser',  methods=['GET', 'POST'])
def createuser():
    form = Createlogin()
    
    if form.validate_on_submit():
        
        return render_template('createRequest.html', form=form)

    
    return redirect(location=url_for("loginform"))

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
    print(user.query.all())
    return user1password