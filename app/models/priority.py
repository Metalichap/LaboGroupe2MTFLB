from app import db
from app.models.base_entity import BaseEntity

class Priority(BaseEntity, db.Model):
    """

    """

    __tablename__ = "priorities"

    priority_id = db.Column(db.Integer, primary_key=True)
    priority_name = db.Column(db.String(31), unique=True, nullable=False, index=True)
    priority_level = db.Column(db.Integer, nullable=False)
    priority_delay_hours = db.Column(db.Integer, nullable=False)

    tickets = db.relationship('Ticket', back_populates='priority')




