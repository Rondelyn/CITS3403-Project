from unittest import TestCase

from app import create_app, db
from app.config import TestConfig
from app.controllers import registration, UserCreationError


class BasicUnitTests(TestCase):

    def setUp(self):
        testApp = create_app(TestConfig)
        self.app_context = testApp.app_context()
        self.app_context.push()
        db.create_all()
        

    def tearDown(self):
        db.sessioin.remove()
        db.drop_all()
        self.app_context.pop()

    def test_registration_same_user(self):
        with self.assertRaises(UserCreationError):
            registration('1234','1234')