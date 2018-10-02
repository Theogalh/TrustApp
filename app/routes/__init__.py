from flask import render_template, flash, redirect, url_for
from app import app, db
from .login import login
from .logout import logout
from .register import register
from .user import user
from .list import list
from flask_login import login_required, current_user
from datetime import datetime


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
