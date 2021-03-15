from wtforms import StringField, PasswordField, Form
from wtforms.validators import DataRequired

class UserForm(Form):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])