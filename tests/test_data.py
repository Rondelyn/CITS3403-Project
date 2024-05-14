from app import db
from app.model import *


user1 = user(id = '1234', user_password = '1234')
user2 = user(id = '12345678', user_password = '12345678')
user3 = user(id = '1234321', user_password = '1234321')

def add_test_users_to_db():
    db.session.add_all([user1,user2,user3])
    db.session.commit()
