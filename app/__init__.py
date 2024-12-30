from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy # for object-relational mapping (ORM)
from flask_migrate import Migrate # fore migration when database schema changes
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
# For each extension, we need to create an object for it
app = Flask(__name__) # Create an instance of the Flask class
app.config.from_object(Config) # Use this code helps us to load the configuration from the Config class
db = SQLAlchemy(app) # Create a database instance
migrate = Migrate(app, db) # create a migration engine, it isn't necessary for starter, but worth to have
# it is used when we want to change the database schema (structure) without recreating the database
# it will create a migration repository which stores how the database changes in python scripts

login = LoginManager(app)
login.login_view = 'login'

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

from app import routes, models, errors # models is the place where data is stores as a list of classes

