# Licensed under GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.en.html

"""For now, just the home page route."""

from flask_login import current_user, login_user

from app import app
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    """Simple hello world test."""
    return "Hello world"

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
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
