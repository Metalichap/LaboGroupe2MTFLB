from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional


class TeamInsertForm(FlaskForm):
    team_name = StringField('team_name', validators=[DataRequired(), Length(min=3, max=127)])
    team_description = TextAreaField('team_description', validators=[Optional()])

class TeamUpdateForm(FlaskForm):
    pass