from app import app, db
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from app.forms.list import ListCreateForm
from app.forms.character import CharacterCreateForm
from app.models.list import List
from app.models.character import Character
from werkzeug.urls import url_parse

