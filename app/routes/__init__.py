from flask import render_template, flash, redirect, url_for
from app import app, db
from .login import login
from .logout import logout
from .register import register
from .user import user
from flask_login import login_required, current_user
from datetime import datetime


@app.route('/')
@app.route('/index')
@login_required
def index():
    players = [
        {
            "name": "Theogalh",
            "ilvl": 368,
            "role": "tank"
        },
        {
            "name": "Geoffrey",
            "ilvl": 377,
            "role": "Heal"
        },
        {
            "name": "Magnus",
            "ilvl": 364,
            "role": "Range"
        },

    ]
    return render_template('index.html', title='Home', players=players)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
