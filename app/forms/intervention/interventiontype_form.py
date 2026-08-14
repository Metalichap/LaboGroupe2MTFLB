from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, length


class InterventionTypeForm(FlaskForm):

    name = StringField("Nom du type d'intervention", validators=[DataRequired(), length(min=2, max=127)])
    description = TextAreaField("Description", validators=[DataRequired()])