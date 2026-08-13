from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional


class CategoryForm(FlaskForm):
    category_name = StringField('category_name', validators=[DataRequired(), Length(max=127)])
    category_description = TextAreaField('category_description', validators=[Optional()])