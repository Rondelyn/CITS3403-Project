from wtforms import StringField, SubmitField, BooleanField, SelectField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, InputRequired, Length, ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed
from app.model import image, user
from wtforms import widgets, SelectMultipleField, SelectField

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class Createpost(FlaskForm):
    title = StringField("Post Title", render_kw = {'id': 'title'}, validators = [DataRequired()])
    image = FileField('Upload Image', render_kw = {'id': "imgUpload"}, validators=[FileRequired('File missing'), FileAllowed(['jpg','png','jpeg'])])
    user_id = StringField("User ID", render_kw={'style': 'display:none'})
    submit = SubmitField("Create post")
    catagories =  MultiCheckboxField('Categories', 
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
                                    render_kw = {'class':'form-check-input me-1'}
                                    
                                    )

class postform(FlaskForm):
    user_id = StringField("User ID", render_kw={'style': 'display:none'})
    title = StringField("Post Title", render_kw = {'id': 'title'}, validators = [DataRequired()])
    image = FileField('Upload Image', render_kw = {'id': "imgUpload"}, validators=[FileRequired('File missing'), FileAllowed(['jpg','png','jpeg'])])
    catagories =  MultiCheckboxField('Categories',
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
                                    render_kw = {'class':'form-check-input me-1'}
                                    )
    
    star = SubmitField("submit rating", render_kw={"onclick": "getrating()"})
    starvalue = SelectField("Category", choices = ['1', '2', '3', '4', '5'])
    
    
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





class RegisterForm(FlaskForm):
    id = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    user_password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')
    checkbox = BooleanField(label='You agree not to post silly things', render_kw={'checked': False}, validators = [DataRequired()])


        

class LoginForm(FlaskForm):
    id = StringField(validators=[
                        InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    user_password = PasswordField(validators=[
                            InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')

    def is_authenticated(self):
        return self.authenticated
    
class deleate(FlaskForm):
    reason = StringField("report reason", render_kw = {'id': 'reason'}, validators = [DataRequired()])
    submitreason = SubmitField('report')





    