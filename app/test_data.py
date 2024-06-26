
from app import db, bcrypt
from app.model import *



def add_test_users_to_db():
    user1 = user(id = '12341234', user_password = bcrypt.generate_password_hash('12341234'))
    user2 = user(id = '12345678', user_password = bcrypt.generate_password_hash('12345678'))
    user3 = user(id = '1234321', user_password = bcrypt.generate_password_hash('1234321'))

    db.session.add_all([user1,user2,user3])
    db.session.commit()

def add_test_images_to_db():
    image1 = image(image_url='img1.jpg', image_catagroy='Women', image_likes=1, title='hi there', user_id='12345678')
    image2 = image(image_url='img2.jpg', image_catagroy='Men', image_likes=2, title= 'yesss', user_id='12345678')
    image3 = image(image_url='img3.jpg', image_catagroy='Men', image_likes=3, title= 'photo', user_id='1234321')

    db.session.add_all([image1,image2,image3])
    db.session.commit()