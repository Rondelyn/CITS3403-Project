from unittest import TestCase

from app import create_app, db
from app.config import TestConfig, DeploymentConfig
from app.controllers import *
from app.test_data import add_test_users_to_db, add_test_images_to_db




class BasicUnitTests(TestCase):

    def setUp(self):
        print("6666666666666")
        testApp = create_app(DeploymentConfig)
        print("99999999")
        self.app_context = testApp.app_context()
        print("hfhhf")
        self.app_context.push()
        print("kjashdkjh")
        db.create_all()
        print("111111111")
        add_test_users_to_db()
        print("22222222222")
        add_test_images_to_db()
        

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()



    def test_registration_of_user_that_exists(self):
        print("kjsdhfkjahkdhfau")
        with self.assertRaises(UserCreationError):
            registration('1234','1234')



 
