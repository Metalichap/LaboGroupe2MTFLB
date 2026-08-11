from app import db
from app.models.base_entity import BaseEntity

class TicketTag(BaseEntity, db.Model):
    """

    """
    __tablename__ = 'ticket_tags'

    ticket_id = db.Column(db.ForeignKey("tickets.ticket_id"), primary_key=True)
    tag_id = db.Column(db.ForeignKey("tags.tag_id"), primary_key=True)

    ticket = db.relationship('Ticket', back_populates="tags")
    tag = db.relationship('Tag', back_populates="tickets")




