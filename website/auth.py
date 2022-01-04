from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return '<p>Logout</p>'

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method=="POST":
        email= request.form.get('email')
        firstName = request.get('firstName')
        password1= request.get('password1')
        password2 = request.get('password2')

    return render_template('sign_up.html')