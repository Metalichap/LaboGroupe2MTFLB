from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField, DateTimeLocalField
from wtforms.validators import DataRequired, InputRequired, NumberRange


class InterventionForm(FlaskForm):

    date = DateTimeLocalField("Date du début de l'intervention", format="%Y-%m-%dT%H:%M", validators=[DataRequired()])
    duration = IntegerField("Durée de l'intervention (en minutes)", validators=[InputRequired(), NumberRange(min=0)])
    report = TextAreaField("Rapport", validators=[DataRequired()])
