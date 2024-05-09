from wtforms import StringField, SubmitField, BooleanField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import widgets, SelectMultipleField, SelectField


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class Createpost(FlaskForm):
    title = StringField("Post Title", render_kw = {'id': 'title'}, validators = [DataRequired()])
    image = FileField('Upload Image', render_kw = {'id': "imgUpload"}, validators=[FileRequired('File missing'), FileAllowed(['jpg','png'])])
    submit = SubmitField("Create post")
    categories = MultiCheckboxField('Categories',
                                    choices=[('Women', 'Women'), 
                                             ('Mens', 'Mens'), 
                                             ('Unisex', 'Unisex'), 
                                             ('Vintage', 'Vintage'),
                                             ('OfficeCore', 'Office Core'),
                                             ('Y2K', 'Y2K'),
                                             ('CottageCore', 'Cottage Core'),
                                             ('GothCore', 'Goth Core'),
                                             ('CyberPunk', 'CyberPunk'),
                                             ('Dogs', 'Dogs'),
                                             ('Cats', 'Cats')],
                                    render_kw = {'class':'no_bullets'}
                                    )
                                             

class catergoryFilter(FlaskForm):
    submitfilter = SubmitField("Filter Posts")
    filter = SelectField('Filters', 
                                 choices =[('Women', 'Women'), 
                                             ('Mens', 'Mens'), 
                                             ('Unisex', 'Unisex'), 
                                             ('Vintage', 'Vintage'),
                                             ('OfficeCore', 'Office Core'),
                                             ('Y2K', 'Y2K'),
                                             ('CottageCore', 'Cottage Core'),
                                             ('GothCore', 'Goth Core'),
                                             ('CyberPunk', 'CyberPunk'),
                                             ('Dogs', 'Dogs'),
                                             ('Cats', 'Cats')], )
    
    

class Createlogin(FlaskForm):
    username = StringField("Username", render_kw = {'id': 'signInputUsername'}, validators = [DataRequired()])
    password = StringField("Password", render_kw = {'id': 'signPassword'}, validators = [DataRequired()])
    checkbox = BooleanField(label='You agree not to post silly things', render_kw={'checked': False}, validators = [DataRequired()])
    createuser = SubmitField("Create user",render_kw = {'id': 'sign-submite'},  validators = [DataRequired()])
    submitlogin = SubmitField("login",render_kw = {'id': 'sign-submite'},  validators = [DataRequired()])


    