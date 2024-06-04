from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required
from web.models.user import User
from web import db


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash("Signed in successfully", category="success")
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash("Invalid Email", category='error')
        
    return render_template('login.html', user=current_user)
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', category='success')
    return redirect(url_for('auth.login'))  # Redirect to login or home page


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')  # Corrected form field name
        second_name = request.form.get('second_name')  # Corrected form field name
        password = request.form.get('password')
        password2 = request.form.get('confirm-password')
        age = int(request.form.get('age'))  # Convert age to integer
        phoneN = request.form.get('phoneN')
        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists.', category='error')
        elif  len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif age < 18:  # Check if age is less than 18
            flash('Age must be 18 or greater.', category='error')
        elif len(first_name) < 2 or len(second_name) < 2:
            flash('First name and second name must be greater than 1 character.', category='error')
        elif len(phoneN) != 11:
            flash('Phone number must be 11 characters.', category='error')
        elif password != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
    # Create new user
            new_user = User(
            email=email,
            first_name=first_name,
            second_name=second_name,
            password=generate_password_hash(password, method='sha256'),
            age=age,
            phone_number=phoneN
            )
            db.session.add(new_user)
            db.session.commit()
    
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html', user=current_user)
