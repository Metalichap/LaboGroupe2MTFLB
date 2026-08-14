from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Length


class SiteForm(FlaskForm):
    """
    """
    name = StringField('Nom', validators=[DataRequired(), Length(min=2, max=127)])
    address = StringField('Adresse', validators=[Length(min=2, max=255)])
    city = StringField('Ville', validators=[Length(min=2, max=63)])
    
