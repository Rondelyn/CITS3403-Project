from wtforms import StringField, SubmitField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class Createpost(FlaskForm):
    title = StringField("Post Title", render_kw = {'id': 'title'}, validators = [DataRequired()])
    image = FileField('Upload Image', render_kw = {'id': "imgUpload"}, validators=[FileRequired('File missing')])
    submit = SubmitField("Create post")


class Createlogin(FlaskForm):
    username = StringField("Username", render_kw = {'id': 'signInputUsername'}, validators = [DataRequired()])
    password = StringField("Password", render_kw = {'id': 'signPassword'}, validators = [DataRequired()])
    checkbox = BooleanField(label='You agree not to post silly things', render_kw={'checked': False}, validators = [DataRequired()])
    createuser = SubmitField("Create user",render_kw = {'id': 'sign-submite'},  validators = [DataRequired()])
    submitlogin = SubmitField("login",render_kw = {'id': 'sign-submite'},  validators = [DataRequired()])


    