from app import db
from app.models.base_entity import BaseEntity

class Tag(BaseEntity, db.Model):
    """

    """
    __tablename__ = 'tags'

    tag_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_name = db.Column(db.String(63), unique=True, index=True, nullable=False)
    tag_color = db.Column(db.String(8), nullable=False)

    tickets = db.relationship('TicketTag', back_populates='tag')

