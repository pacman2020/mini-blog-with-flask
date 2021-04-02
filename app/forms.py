from wtforms import (
    StringField, 
    Form, 
    FileField, 
    TextAreaField)
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired

class LoginForm(Form):
    email = StringField('E-mail', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class UserForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class UserFormUpdate(Form):
    username = StringField('Username', validators=[DataRequired()])
    
class PublicationForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    photo = FileField('Photo')
    description = TextAreaField('description', validators=[DataRequired()])