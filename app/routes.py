# app/routes.py
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from .forms import RegistrationForm, LoginForm, TaskForm
from .models import User, Task
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('main', __name__)

@main.route('/')
# @login_required
def home():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.html'))
    return render_template('home.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)  # Assuming you're using Flask-Login
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        errors = False
        
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'danger')
            errors = True
        
        existing_email = User.query.filter_by(email=form.email.data).first()
        if existing_email:
            flash('Email already exists. Please choose a different one.', 'danger')
            errors = True
        
        if form.password.data != form.confirm_password.data:
            flash('Passwords do not match. Please try again.', 'danger')
            errors = True
        
        if errors:
            return redirect(url_for('main.register'))
        
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        new_user = User(firstname=form.firstname.data,
                        lastname=form.lastname.data,
                        username=form.username.data, 
                        email=form.email.data, 
                        password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/dashboard')
@login_required
def dashboard():
    #  tasks = Task.query.filter_by(user_id=current_user.id).all()
    # return render_template('dashboard.html', tasks=tasks)
    return render_template('dashboard.html')

@main.route('/tasks')
@login_required
def tasks():
    user_tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', tasks=user_tasks)

@main.route('/create-task', methods=['GET', 'POST'])
@login_required
def create_task():
    # task creation logic here
    pass

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))