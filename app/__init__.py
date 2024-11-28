from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy # for object-relational mapping (ORM)
from flask_migrate import Migrate # fore migration when database schema changes
app = Flask(__name__) # Create an instance of the Flask class
app.config.from_object(Config) # Use this code helps us to load the configuration from the Config class
db = SQLAlchemy(app) # Create a database instance
migrate = Migrate(app, db) # create a migration engine, it isn't necessary for starter, but worth to have
# it is used when we want to change the database schema (structure) without recreating the database
# it will create a migration repository which stores how the database changes in python scripts

from app import routes, models # models is the place where data is stores as a list of classes