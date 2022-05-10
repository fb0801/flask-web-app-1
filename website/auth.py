import re
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='POST':
        email = request.form.get("email")
        password = request.get("password")


        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category="success")
                return redirect(url_for('views.home'))
            else:
                flash("incorrect, try again!", category="error")
        else:
            flash("email does not exist!", category="error")
    return render_template("login.html", booLean= True)
   # data = request.form
  #  return render_template('login.html')


@auth.route('/logout')
def logout():
    return '<p>Logout</p>'

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method=="POST":
        email= request.form.get('email')
        first_name = request.form.get('firstName')
        password1= request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash("email already exists", category="error")
        elif len(email) < 4:
            flash('Email must be greater than 3 character', category='error')
        elif len(first_name) < 2:
            flash('firstname must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('passwords dont match', category='error')
        elif len(password1) < 7:
            flash('password must be at least 7 characters', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account made!', category='success')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html')