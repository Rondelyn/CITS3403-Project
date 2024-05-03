from app import db
from app.model import *


image1  = image(image_url= "https://i.pinimg.com/originals/e2/5b/af/e25baf3b45328c069181aa7a2f723486.jpg", image_catagroy= "fit", user_id="john", image_id=1, image_likes=0)
image2  = image(image_url= "https://i.pinimg.com/originals/85/64/b8/8564b8ed9eb207042010c46ab0bdf973.jpg", image_catagroy= "fit", user_id="john", image_id=2, image_likes=0)
image3  = image(image_url= "https://i.pinimg.com/564x/04/f6/88/04f68836a0efb96d1c1c04e52b7aab86.jpg", image_catagroy= "fit", user_id="john", image_id=3, image_likes=0)
image4  = image(image_url= "https://i.pinimg.com/564x/16/ae/83/16ae832552ff673fc5496e623f562200.jpg", image_catagroy= "fit", user_id="john", image_id=4, image_likes=0)
image5  = image(image_url= "https://i.pinimg.com/736x/cf/1c/f6/cf1cf679e2720f6d3de6c9d3ba18162c.jpg", image_catagroy= "fit", user_id="john", image_id=5, image_likes=0)


user1 = user(user_id="001", user_password="1234")

db.session.add_all([image1,image2,image3,image4,image5,user1])
db.session.commit()


