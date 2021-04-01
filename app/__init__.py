from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

#redirecionamento de rotas privadas
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return UserModel.get(user_id)

#config keys, sqlalchemy
app.config.from_object('config')

db = SQLAlchemy(app)
Migrate(app, db)


#models
from .models.User import UserModel
from .models.Publication import PublicationModel


#controllers
from .controllers import userController, publicationController