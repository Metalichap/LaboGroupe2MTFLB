from app import db
from app.models.base_entity import BaseEntity
import enum

class PriorityLevel(enum.Enum):
    URGENT = 1
    NORMAL = 2
    LOW = 3

class Priority(BaseEntity, db.Model):
    """

    """

    __tablename__ = "priorities"

    priority_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    priority_name = db.Column(db.String(31), unique=True, nullable=False, index=True)
    priority_level = db.Column(db.Enum(PriorityLevel), default=PriorityLevel.NORMAL, nullable=False)
    priority_delay_hours = db.Column(db.Integer, nullable=False)

    tickets = db.relationship('Ticket', back_populates='priority')




