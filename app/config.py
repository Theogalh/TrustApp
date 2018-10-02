import os

POSTGRE = {
    'user': 'trustapp',
    'pw': 'root123',
    'db': 'trustapp',
    'host': 'localhost',
    'port': '5432'
}


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "postgresql://{}:{}@{}:{}/{}".format(POSTGRE['user'],
                                                                                                     POSTGRE['pw'],
                                                                                                     POSTGRE['host'],
                                                                                                     POSTGRE['port'],
                                                                                                     POSTGRE['db'])
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGGING_DIR = os.environ.get('LOGGING_DIR') or '/var/log/trustapp.log'
