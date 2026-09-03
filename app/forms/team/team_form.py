from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional


class TeamForm(FlaskForm):
    team_name = StringField('team name', validators=[DataRequired(), Length(min=3, max=127)])
    team_description = TextAreaField('team description', validators=[Optional()])
