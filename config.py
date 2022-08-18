import os
basedir = os.path.abspath(os.path.dirname(__file__))

   
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') #for CSRF Form protection
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    #SQLALCHEMY_TRACK_MODIFICATIONS = False