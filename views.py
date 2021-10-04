from setup import app
from flask import render_template,redirect,url_for,flash
from flask_googlemaps import Map
from models.database import users,db
from models.form_models import RegistrationForm,LoginForm

@app.route('/')
def home():
    chuka_uni = Map(
        identifier="chuka_uni",
        lat= -0.319144,
        lng= 37.6528496,
        markers=[{
            'icon':'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
            'lat': -0.319144,
            'lng':37.6528496,
            'infobox':'<b>pavillion</b>',
            'region':'KE',
        }]
    )
    return render_template('home.html',mymap=chuka_uni)

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.is_submitted():
        reg_validation = users.query.filter_by(reg_no=form.reg_no.data).first()
        email_validation = users.query.filter_by(email=form.email.data).first()
        number_validation = users.query.filter_by(phone_number=form.phone_number.data).first()
        if not reg_validation:
            if not email_validation:
                if not number_validation:
                    user_data = users(name=form.name.data,reg_no=form.reg_no.data,
                                        email=form.email.data,
                                        phone_number=form.phone_number.data,
                                        password = form.password.data)
                    db.session.add(user_data)
                    db.session.commit()
                    flash('You have successfully registered')
                    return redirect(url_for('login'))
                flash('number already in use')
            flash('Email already in use')
        flash('user already exists')
    return render_template('registration.html',form=form)

from flask import session

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.is_submitted():
        logging_user = users.query.filter_by(reg_no=form.reg_no.data).first()
        if logging_user:
            flash('sucessfully logged in')
            session['user'] = form.reg_no.data 
            return redirect(url_for('home'))
        flash('Please register first')
    return render_template('login.html',login_form=form)

@app.route('/logout')
def logout():
    flash('successfully logged out')
    session['user'] = ''
    return redirect(url_for('login'))