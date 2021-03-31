from flask import (
    Flask, 
    request,
    render_template, 
    redirect, url_for,
    session)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_login import (
    LoginManager, 
    UserMixin, 
    login_user, 
    logout_user, 
    login_required)

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

#config
app.config.from_object('config')

db = SQLAlchemy(app)
Migrate(app, db)

#models
from .models.User import UserModel
from .models.Publication import PublicationModel


#controllers
from .controllers import userController, publicationController