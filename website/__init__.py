from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, current_user, login_required
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash


db = SQLAlchemy()
DB_NAME = "database.db"
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['ADMIN_PASSWORD_HASH'] = generate_password_hash('aya1234')  # Hash the password


    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    from .models import User, Note
    
    with app.app_context():
        db.create_all()
        populate_cars()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
from .models import Car

def populate_cars():
    # Example data, replace with real data
    cars = [
        Car(make='Toyota', model='Camry', year=2021, color='Red', description='A reliable sedan for everyday use'),
        Car(make='Honda', model='Accord', year=2020, color='Blue', description='Spacious and fuel-efficient'),
        Car(make='Ford', model='Mustang', year=2019, color='Yellow', description='Iconic American muscle car'),
        Car(make='Chevrolet', model='Camaro', year=2022, color='Black', description='Sporty and powerful'),
        Car(make='Tesla', model='Model 3', year=2021, color='White', description='Electric sedan with advanced features'),
        Car(make='byd', model='Model', year=2025, color='White', description='Electric sedan with advanced features'),

       ]
    db.session.add_all(cars)
    db.session.commit()

    
from .models import Reservation

def car_details(car_id):
    car = Car.query.get_or_404(car_id)
    return render_template('cars.html', car=car)


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')