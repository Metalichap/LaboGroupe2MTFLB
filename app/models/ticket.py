from app import db
from app.models.base_entity import BaseEntity
import enum

class TicketStatus(enum.Enum):
    NEW = 'nouveau'
    PENDING = 'en cours'
    SOLVED = 'résolu'
    CLOSED = 'fermé'

class Ticket(BaseEntity, db.Model):
    """

    """

    __tablename__ = 'tickets'

    ticket_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticket_title = db.Column(db.String(63), nullable=False)
    ticket_description = db.Column(db.Text)
    ticket_status = db.Column(db.Enum(TicketStatus), default=TicketStatus.NEW, nullable=False)
    ticket_due_date = db.Column(db.DateTime(timezone=True), nullable=True)

    author_id = db.Column(db.ForeignKey('users.user_id'), nullable=False)
    technician_id = db.Column(db.ForeignKey('users.user_id'), nullable=True)
    category_id = db.Column(db.ForeignKey('categories.category_id'), nullable=False)
    priority_id = db.Column(db.ForeignKey('priorities.priority_id'), nullable=False)
    equipment_id = db.Column(db.ForeignKey('equipments.equipment_id'), nullable=True)
    
    author = db.relationship('User',foreign_keys=[author_id],back_populates='tickets_created')
    technician = db.relationship('User',foreign_keys=[technician_id],back_populates='tickets_assigned'    )
    category = db.relationship('Category', back_populates='tickets')
    priority = db.relationship('Priority', back_populates='tickets')
    equipments = db.relationship('Equipment', back_populates='tickets')
    interventions = db.relationship('Intervention', back_populates='ticket')
    tags = db.relationship('TicketTag', back_populates='ticket')

    comments = db.relationship('Comment', back_populates='ticket')
    histories = db.relationship('TicketStatusHistory', back_populates='ticket')
    attachments = db.relationship('Attachment', back_populates='ticket')
    survey = db.relationship('SatisfactionSurvey', back_populates='ticket')

