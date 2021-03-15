from wtforms import StringField, PasswordField, Form
from wtforms.validators import DataRequired

class UserForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])