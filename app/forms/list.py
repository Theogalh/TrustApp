from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class ListCreateForm(FlaskForm):
    name = StringField("List Name", validators=[DataRequired()])
    submit = SubmitField("Create List")
