from flask import (
    Flask, 
    request, 
    render_template, 
    redirect
    )
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

#config
app.config.from_object('config')

db = SQLAlchemy(app)
Migrate(app, db)

#models
from .models.User import UserModel

#controllers
from .controllers import userController
