from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,InputRequired
from wtforms.validators import EqualTo
from wtforms import StringField,IntegerField,PasswordField,SubmitField,TimeField,DateField
from flask_wtf import FlaskForm


# registration form class model which inherits from the flask form object
class RegistrationForm(FlaskForm):
    name = StringField(validators=[InputRequired()])
    reg_no = StringField(validators=[DataRequired(),InputRequired()])
    email= StringField(validators=[InputRequired()])
    phone_number = IntegerField(validators=[InputRequired()])
    password = PasswordField(validators=[DataRequired(),InputRequired()])
    Register = SubmitField('REGISTER')

# log in form model
class LoginForm(FlaskForm):
    reg_no = StringField(validators=[DataRequired(),InputRequired()])
    password = PasswordField(validators=[InputRequired()])
    confirm_password = PasswordField(validators=[InputRequired(),EqualTo(password)])
    login = SubmitField('LOG IN')

# location details form model
class Default(FlaskForm):
    name = StringField(validators=[InputRequired()])
    time = TimeField(validators=[DataRequired(),InputRequired()])
    date = DateField(validators=[DataRequired(),InputRequired()])

class Custom(Default):
    loc_lat = StringField(validators=[InputRequired()])
    loc_longt = StringField(validators=[InputRequired()])

