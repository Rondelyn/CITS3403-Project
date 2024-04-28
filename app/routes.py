
from flask import render_template
from app import flaskApp
from app.model import image
from app.model import topimages

image1 = image(imageurl = "/static/example-imgs/img1.jpg", imagecatagroy= "01")
image2 = image(imageurl = "/static/example-imgs/img2.jpg", imagecatagroy= "02")
image3 = image(imageurl = "/static/example-imgs/img3.jpg", imagecatagroy= "03")
image4 = image(imageurl = "/static/example-imgs/img4.jpg", imagecatagroy="04")

top4image = topimages(images=[image1,image2,image3,image4])

alltopimage = [top4image]

@flaskApp.route("/")    
@flaskApp.route("/landingPg")
def topimage():
    return render_template("landingPg.html", topimage=alltopimage)

@flaskApp.route("/login")
def loginform():
    return render_template("login.html")

@flaskApp.route("/findRequest")
def posts():
    return render_template("findRequest.html")

@flaskApp.route("/createRequest")
def post():
    return render_template("createRequest.html")


