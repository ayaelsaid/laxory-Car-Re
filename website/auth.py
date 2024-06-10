from flask import Blueprint, current_app, jsonify, render_template, request, flash, redirect, session, url_for
from .models import User, Car, Reservation, Process, Note
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
import datetime  # Import datetime module
from website import bcrypt
import json


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('auth.my_reservations'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)  # Log the user in
            flash('Account created!', category='success')
            return redirect(url_for('auth.my_reservations'))  # Redirect to my_reservations

    return render_template("sign_up.html", user=current_user)
@auth.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password = request.form.get('password')

        user = User.query.filter_by(id=current_user.id).first()
        user.email = email
        user.first_name = first_name
        if password:
            user.password = generate_password_hash(password, method='sha256')
        db.session.commit()

        flash('Information updated successfully!', category='success')

    return render_template("settings.html", user=current_user)

@auth.route('/delete-account', methods=['POST'])
@login_required
def delete_account():
    user = User.query.filter_by(id=current_user.id).first()
    db.session.delete(user)
    db.session.commit()
    logout_user()
    flash('Account deleted successfully!', category='success')
    return redirect(url_for('auth.sign_up'))

@auth.route('/cars')
def cars():
    cars = Car.query.all()
    return render_template('cars.html', cars=cars, user=current_user)
#@auth.route('/reservation/<int:car_id>')
@auth.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        # Get the form data
        car_id = request.form['car_id']
        start_date = datetime.datetime.strptime(request.form['start_date'], '%Y-%m-%d')
        end_date = datetime.datetime.strptime(request.form['end_date'], '%Y-%m-%d')
        age = request.form['age']
        phone_number = request.form['phone_number']
        license_copy = request.form['license_copy']
        personal_id_copy = request.form['personal_id_copy']
        payment_method = request.form['payment_method']
        
        # Create a new reservation
        reservation = Reservation(car_id=car_id, start_date=start_date, end_date=end_date, age=age, phone_number=phone_number,
                                license_copy=license_copy, personal_id_copy=personal_id_copy, payment_method=payment_method)
        # Save the reservation to the database
        db.session.add(reservation)
        db.session.commit()
        
        # Redirect to the reservation success page with the reservation_id
        return redirect(url_for('auth.reservation_success', reservation_id=reservation.id))  # Pass reservation_id
        
    # Render the reservation page
    return render_template('reservation.html', user=current_user)

@auth.route('/reservation_success/<int:reservation_id>')
@login_required
def reservation_success(reservation_id):
    # Fetch the reservation details
    reservation = Reservation.query.get(reservation_id)
    if not reservation:
        return "Reservation not found", 404

    # Fetch the car details
    car = Car.query.get(reservation.car_id)
    if not car:
        return "Car not found", 404

    return render_template('reservation_success.html', user=current_user, car=car, reservation=reservation)

@auth.route('/confirm_reservation/<int:reservation_id>', methods=['POST'])
@login_required
def confirm_reservation(reservation_id):
    reservation = Reservation.query.get(reservation_id)
    if not reservation:
        flash("Reservation not found")
        return redirect(url_for('auth.reservation_success'))

    # Update the reservation status to confirmed
    reservation.confirmed = True
    db.session.commit()

    # Create a new entry in the Process table
    process = Process(
        user_id=current_user.id,
        reservation_id=reservation.id,
    )
    db.session.add(process)
    db.session.commit()

    flash("Reservation confirmed successfully!")
    return redirect(url_for('auth.my_reservations'))

@auth.route('/my_reservations')
@login_required
def my_reservations():
    # Fetch all confirmed reservations from the Process table
    confirmed_reservations = Process.query.filter_by(user_id=current_user.id).all()
    # Initialize an empty list to store confirmed reservation details
    reservation_details = []
    for process in confirmed_reservations:
        # Fetch reservation details using the reservation_id
        reservation = process.reservation
        car = reservation.car
        # Append reservation details to the list
        reservation_details.append({
            'reservation_id': reservation.id,
            'car_id': car.id,
            'make': car.make,
            'model': car.model,
            'start_date': reservation.start_date,
            'end_date': reservation.end_date,
            'age': reservation.age,
            'phone_number': reservation.phone_number,
            'license_copy': reservation.license_copy,
            'personal_id_copy': reservation.personal_id_copy,
            'payment_method': reservation.payment_method
        })

    # Render the template outside the loop
    return render_template('my_reservations.html', reservations=reservation_details, user=current_user)

@auth.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        password = request.form.get('password')
        admin_password_hash = current_app.config['ADMIN_PASSWORD_HASH']
        if check_password_hash(admin_password_hash, password):
            session['admin_logged_in'] = True
            flash('Admin login successful!', 'success')
            return redirect(url_for('auth.admin_dashboard'))
        else:
            flash('Incorrect admin password', 'error')
    return render_template('admin/admin_login.html', user=current_user)

@auth.route('/admin/dashboard')
def admin_dashboard():
    if session.get('admin_logged_in'):
        return render_template('admin/dashboard.html', user=current_user)
    else:
        return "You are not authorized to access this page.", 403

@auth.route('/admin/logout')
@login_required
def admin_logout():
    session.pop('admin_logged_in', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('auth.admin_login'))
@auth.route('/note', methods=['GET', 'POST'])
@login_required
def note():
    if request.method == 'POST': 
        note_text = request.form.get('note')

        if len(note_text) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note_text, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    notes = Note.query.filter_by(user_id=current_user.id).all()
    return render_template("note.html", user=current_user, notes=notes)

@auth.route('/delete-note', methods=['POST', 'GET'])
def delete_note():  
    data = json.loads(request.data)
    note_id = data.get('noteId')
    if note_id:
        note = Note.query.get(note_id)
        if note and note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            return jsonify({'message': 'Note deleted successfully'})
    
    return jsonify({'error': 'Failed to delete note'}), 400
