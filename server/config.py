import os


class BaseConfig(object):
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = os.environ['DEBUG']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
