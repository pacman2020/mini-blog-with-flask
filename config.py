import os
from os.path import dirname, realpath


UPLOAD_FOLDER = os.path.join(dirname('app/static/uploads/'))
SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'senha-muito-forte'

DEBUG = 'True'