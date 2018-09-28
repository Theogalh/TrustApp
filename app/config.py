import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL') or "postgresql://localhost/wordcount_dev"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
