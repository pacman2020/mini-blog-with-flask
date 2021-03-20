import os


UPLOAD_FOLDER = os.path.join(os.getcwd(),'uploads')
SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'senha-muito-forte'

DEBUG = 'True'