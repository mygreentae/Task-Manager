# app/routes.py
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
# from .forms import RegistrationForm, LoginForm, TaskForm
# from .models import User, Task
from . import db

main = Blueprint('main', __name__)

@main.route('/')
# @login_required
def home():
    return render_template('home.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    pass

@main.route('/register', methods=['GET', 'POST'])
def register():
    # registration logic here
    pass

@main.route('/create-task', methods=['GET', 'POST'])
@login_required
def create_task():
    # task creation logic here
    pass

@main.route('/logout')
@login_required
def logout():
    # logout logic here
    pass