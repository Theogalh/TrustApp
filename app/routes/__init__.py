from flask import render_template, flash, redirect, url_for
from app import app
from .login import login
from .logout import logout
from .register import register
from flask_login import login_required


@app.route('/')
@app.route('/index')
@login_required
def index():
    players = [
        {
            "name": "Théogalh",
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
