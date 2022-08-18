import os
basedir = os.path.abspath(os.path.dirname(__file__))

   
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is just a placeholder' #for CSRF Form protection
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = 'postgres://bosteqblluxeud:f2dca933005930b96e2c012f3a69b55d504c9431f99f1328c94c1487a079ec71@ec2-3-224-184-9.compute-1.amazonaws.com:5432/dd5eq8ac8persf'
    SQLALCHEMY_TRACK_MODIFICATIONS = False