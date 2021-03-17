from wtforms import StringField, Form
from wtforms.validators import DataRequired

class UserForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])

class UserFormUpdate(Form):
    username = StringField('Username', validators=[DataRequired()])