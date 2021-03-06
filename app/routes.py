# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""For now, just the home page route."""

from flask_login import current_user, login_user, logout_user
from flask import render_template, request, url_for, redirect, flash
from werkzeug.urls import url_parse

from app import app, db
from app.models import User
from app.forms import LoginForm, RegistrationForm

@app.route('/')
@app.route('/index')
def index():
    #"""Simple hello world test."""
    #return "Hello world"
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user sign in calls."""
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

# NOTE: add a @login_required after a route
