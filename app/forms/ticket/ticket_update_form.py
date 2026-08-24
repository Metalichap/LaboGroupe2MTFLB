from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateTimeField
from wtforms.validators import DataRequired, Length, Optional


class TicketUpdateForm(FlaskForm):
    ticket_title = StringField('ticket_title', validators=[DataRequired(), Length(max=63)])
    ticket_description = TextAreaField('ticket_description', validators=[Optional()])

    # Choix peuplés par le controller avant le rendu.
    category_id = SelectField('category_id', coerce=int, validators=[DataRequired()])
    priority_id = SelectField('priority_id', coerce=int, validators=[DataRequired()])

    # TicketStatus est un enum Python fixe (pas de la DB): les choix peuvent
    # être posés directement ici, sans requête.
    ticket_status = SelectField('ticket_status', validators=[DataRequired()])

    # Optionnel: un ticket peut rester non assigné. Choix peuplés par le
    # controller (liste des techniciens actifs), '' = non assigné.
    technician_id = SelectField('technician_id', validators=[Optional()])

    def selected_technician_id(self) -> int | None:
        """Convertit la donnée postée (string, potentiellement vide) en int|None."""
        return int(self.technician_id.data) if self.technician_id.data else None