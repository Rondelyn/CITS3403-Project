
#improting required classes
from flask import Flask, render_template, redirect, request, url_for
from app import flaskApp
from flask_sqlalchemy import SQLAlchemy
from app.model import image, user




#createing server connection to web pages so that you can click though them 
#landing page
@flaskApp.route("/")    
@flaskApp.route("/landingPg")
def home():
    return render_template("landingPg.html")

#login page
@flaskApp.route("/login", methods=['GET','POST'])
def loginform():
    form = loginform()
    return render_template("login.html", form = form)


@flaskApp.route("/register", methods=['GET','POST'])
def loginform():
    form = loginform()
    return render_template("login.html", form = form)


#find request page/ posts
@flaskApp.route("/findRequest")
def posts():
    posts = image.query.all()
    return render_template("findRequest.html", images=posts )

#createResquest/ create post
@flaskApp.route("/createRequest")
def images():   
    return render_template("createRequest.html")


