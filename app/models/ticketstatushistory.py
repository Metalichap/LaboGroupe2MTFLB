from app import db
from app.models.base_entity import BaseEntity
from app.models.ticket import TicketStatus

class TicketStatusHistory(BaseEntity, db.Model):
    """

    """

    __tablename__ = "ticketstatushistories"

    history_id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Foreign_key('tickets.ticket_id'), nullable=False)
    user_id = db.Column(db.Foreign_key('users.user_id'), nullable=False)
    old_status = db.Column(db.Enum(TicketStatus))
    new_status = db.Column(db.Enum(TicketStatus))

    ticket = db.relationship('Ticket', back_populates='histories')
    user = db.relationship('User', back_populates='ticket_status_histories')

