
from typing import List
from app import db


#table with post data
class image(db.Model):
    image_url = db.Column(db.String, nullable=False) #add defult = 'default.jpg'?
    image_catagroy = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String(10), db.ForeignKey('user.user_id'), nullable=False)
    image_id = db.Column(db.Integer, primary_key=True)
    image_likes = db.Column(db.Integer)

    

    def __repr__(self) -> str:
        return f'<image {self.user_id} {self.image_id}{self.image_catagroy}>'
    
    def downgrade():
        image.drop_column('image_id')

#table with user data
class user(db.Model):
    user_id = db.Column(db.String(10), primary_key=True)
    user_password = db.Column(db.String (10), nullable=False)

    def __repr__(self) -> str:
        return f'<image {self.user_id} {self.user_password}>'    

    

