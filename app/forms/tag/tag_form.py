from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class TagForm(FlaskForm):

    name = StringField('Nom du Tag', validators=[DataRequired(), Length(min=2, max=63)])
    color = StringField('Couleur (format hex)', validators=[DataRequired(), Length(min=6, max=6)])
