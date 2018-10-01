from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from app.models.character import Character


class CharacterCreateForm(FlaskForm):
    name = StringField("Character Name", validators=[DataRequired()])
    server = StringField("Server", validators=[DataRequired()])
    region = SelectField("Region", validators=[DataRequired()])
    submit = SubmitField("Create Character")


