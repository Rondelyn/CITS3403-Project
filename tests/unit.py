from unittest import TestCase

from app import create_app, db
from app.config import TestConfig, DeploymentConfig
from app.controllers import *
from app.test_data import add_test_users_to_db, add_test_images_to_db




class BasicUnitTests(TestCase):

    def setUp(self):
        testApp = create_app(TestConfig)
        self.app_context = testApp.app_context()
        self.app_context.push()
        db.create_all()
        add_test_users_to_db()
        add_test_images_to_db()
        

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    #execption is thrown when registering with used username
    def test_registration_of_user_that_exists(self):
        print("111111")
        with self.assertRaisesRegex(UserCreationError, "user id: " +  "12341234" + " already exists" ):
            registration('12341234','12341234')
    
    #exception thrown when logging in with unknown username
    def test_login_user_does_not_exist(self):
       print("33333333")
       with self.assertRaisesRegex(UserExistsError, "user id: " +  "898989" + " dose not exist" ):
           login_the_user('898989', '12345678')
       
    #exception thrown when logging in with the wrong password  
    def test_login_password_is_wrong(self):
       with self.assertRaisesRegex(UserExistsError, "password is incorrect" ):
           login_the_user('12341234', '000000000')
           
    #the correct user is returned with logging in with correct password and username
    def test_user_logged_in_successfully(self):
       self.assertEqual( login_the_user('12341234', '12341234'),
                             user(id = '12341234', user_password = bcrypt.generate_password_hash('12341234')))
             
    #exception thrown when report message is not a valid reason    
    def test_deleting_post_not_vaild(self):
        print("2222222")
        with self.assertRaisesRegex(FeedpageUseError, "Not a vaild reason" ):
            reporting_post('12345678', 'I dont like it!!!!!')

    #exception thrown when a image being uploaded has the same name as already uploaded image
    def test_adding_post_with_same_name_to_db(self):
        with self.assertRaisesRegex(NewPostError, "Image with that name already uploaded" ):
            added_image_db('img1.jpg', 'Women', 'hi there', '12345678')
            
   #unique image is uploaded successfully
    def test_added_post_successfully(self):
            added_image_db('img4.jpg', 'Women', 'hi there', '12345678')
