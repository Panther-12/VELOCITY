from flask import Flask
from config import configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_googlemaps import GoogleMaps



# Bind the configuration from the object class
app = Flask(__name__)
app.config.from_object(configuration)

# Attatch sqlalchemy to the app object
db = SQLAlchemy(app)

# Configure flask_migrate to the app object
migrate = Migrate(app,db)

# Initialize the googlemaps extension
GoogleMaps(app)

