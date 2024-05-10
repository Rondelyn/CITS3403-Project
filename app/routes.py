

    #improting required classes
from flask import Flask, render_template, redirect, request, url_for
from app import flaskApp
from flask_sqlalchemy import SQLAlchemy
from app.model import image, user, LoginForm, RegisterForm
from flask_bcrypt import Bcrypt
from app import db
from app.model import *
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user


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
    return render_template("landingPg.html")

#login page
@flaskApp.route("/login", methods=['GET','POST'])
def loginform():
    form = LoginForm()
    if form.validate_on_submit():
        the_user = user.query.filter_by(id=form.id.data).first()
        if the_user:
            if bcrypt.check_password_hash(the_user.user_password, form.user_password.data):
                login_user(the_user)
                return redirect(('/findRequest'))


    
    return render_template("login.html", form=form)


#find request page/ posts
@flaskApp.route("/findRequest" , methods=['GET','POST'])
#@login_required
def posts(): 
    if not current_user.is_authenticated:
        return redirect("/login")
    posts = image.query.all()
    return render_template("findRequest.html", images=posts )

#createResquest/ create post
@flaskApp.route("/createRequest")
def images():   
        if not current_user.is_authenticated:
            return redirect("/login")
        return render_template("createRequest.html")

@flaskApp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('/login')


@ flaskApp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.user_password.data)
        new_user = user(id=form.id.data, user_password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return render_template("findRequest.html", form=form)
    
    return render_template('register.html', form=form)



