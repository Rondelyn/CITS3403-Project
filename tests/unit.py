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
        with self.assertRaises(UserCreationError):
            registration("1234", '1234','1234')

    
    def test_login_user_does_not_exist(self):
        with self.assertRaisesRegex(UserExistsError, "user id: 898989 dose not exist"):
            login_the_user('898989', '12345678')


    def test_login_password_is_wrong(self):
        with self.assertRaisesRegex(UserExistsError, "password is incorrect" ):
            login_the_user('12345678', '000000000')


    def test_deleting_post_not_vaild(self):
        with self.assertRaisesRegex(FeedpageUseError, "Not a vaild reason" ):
            reporting_post('12345678', 'I dont like it!!!!!')

 #   def test_adding_post_with_same_name_to_db(self):
  #      with self.assertRaisesRegex(NewPostError, "Failed to upload image" ):
   #         added_image_db('img1.jpg', 'Women', 'hi there', '12345678')



 
