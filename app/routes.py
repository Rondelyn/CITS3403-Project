
#improting required classes
from flask import render_template, redirect, request, url_for
from app import flaskApp
from app.model import image, user




#createing server connection to web pages so that you can click though them 
#landing page
@flaskApp.route("/")    
@flaskApp.route("/landingPg")
def home():
    return render_template("landingPg.html")

#login page
@flaskApp.route("/login")
def loginform():
    return render_template("login.html")

#find request page/ posts
@flaskApp.route("/findRequest")
def posts():
    return render_template("findRequest.html")

#createResquest/ create post
@flaskApp.route("/createRequest")
def post():
    posts = image.query.all()
    return render_template("createRequest.html", images=posts)


