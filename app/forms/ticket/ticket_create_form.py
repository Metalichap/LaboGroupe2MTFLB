from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateTimeField
from wtforms.validators import DataRequired, Length, Optional


class TicketCreateForm(FlaskForm):
    ticket_title = StringField('ticket_title', validators=[DataRequired(), Length(max=63)])
    ticket_description = TextAreaField('ticket_description', validators=[Optional()])

    category_id = SelectField('category_id', coerce=int, validators=[DataRequired()])
    priority_id = SelectField('priority_id', coerce=int, validators=[DataRequired()])