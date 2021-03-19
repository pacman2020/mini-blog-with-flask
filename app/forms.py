from wtforms import (
    StringField, 
    Form, 
    FileField, 
    TextAreaField)
from wtforms.validators import DataRequired


class UserForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])

class UserFormUpdate(Form):
    username = StringField('Username', validators=[DataRequired()])
    
class PublicationForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    photo = FileField('Photo', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])