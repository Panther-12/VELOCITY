import os

# configuration class

class configuration(object):
    # configure the base path to the database file
    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = 'NIMROD coding Programmer'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,"users.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GOOGLEMAPS_KEY = 'AIzaSyBo6GLAqjGHRs8cuaTg16Jv7b0RaMrlnmY'