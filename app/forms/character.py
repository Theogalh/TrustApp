from wtforms import StringField, SubmitField, SelectField, HiddenField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class CharacterCreateForm(FlaskForm):
    list = HiddenField("List", validators=[DataRequired()])
    name = StringField("Character Name", validators=[DataRequired()])
    server = StringField("Server", validators=[DataRequired()])
    region = SelectField("Region", validators=[DataRequired()],
                         choices=[('EU', 'Europe'), ("KR", "Korea")])
    spe = StringField("Specialisation")
    submit = SubmitField("Create Character")


