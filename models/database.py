from setup import db
from werkzeug.security import generate_password_hash,check_password_hash
import datetime

# users database model/tabel
class users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(24))
    reg_no = db.Column(db.String(13))
    email = db.Column(db.String(64),unique=True)
    phone_number = db.Column(db.Integer,unique=True)
    password_hash = db.Column(db.String(124))

    def __init__(self,name,reg_no,email,phone_number,password):
        self.name = name
        self.reg_no = reg_no
        self.email = email
        self.phone_number = phone_number
        self.password_hash = generate_password_hash(password)

    @property
    def password(self):
        raise AttributeError("password is readable only")

    # generate password hash from the password provided by the user
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    # generates a new hash from the password provided and check against the already 
    # existing hash in the database
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

# location model
class locations(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(24))
    event = db.Column(db.String(64))
    timestamp = db.Column(db.String)
    date_time = db.Column(db.String(64))
    
    def __init__(self,name,event,timestamp,date_time):
        self.name = name
        self.event = event
        self.timestamp = timestamp
        self.date_time = date_time
        