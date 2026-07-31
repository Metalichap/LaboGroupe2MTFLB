from app import db
from app.models.base_entity import BaseEntity

class SatisfactionSurvey(BaseEntity, db.Model):
    """

    """

    __tablename__ = "satisfactionsurveys"

    survey_id = db.Column(db.Integer, primary_key=True)
    survey_rating = db.Column(db.Integer, nullable=False)
    survey_comment = db.Column(db.Text)
    ticket_id = db.Column(db.ForeignKey('tickets.ticket_id'), unique=True, nullable=False)
    client_id = db.Column(db.ForeignKey('users.user_id'), nullable=False)

    ticket = db.relationship('Ticket', back_populates='survey')
    client = db.relationship('User', back_populates='satisfaction_surveys')

