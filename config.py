import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Config isn't necessary for starter, but if you want to have freedom to do things, you need to
# specify the configuration of the app, which can be done in the init file
# However, due to the principle of separation of concerns, we create this file
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')