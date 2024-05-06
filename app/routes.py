
#improting required classes
from flask import render_template, redirect, request, url_for
from app import flaskApp, db
from app.model import image, user




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
    signup = request.args.get('signup', default='false') 
    return render_template("login.html", signup=signup)


#find request page/ posts
@flaskApp.route("/findRequest")
def posts():
    posts = image.query.all()
    return render_template("findRequest.html", images=posts )

#createResquest/ create post
@flaskApp.route("/createRequest")
def images():   
    return render_template("createRequest.html")


