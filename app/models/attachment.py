from app import db
from app.models.base_entity import BaseEntity

class Attachment(BaseEntity, db.Model):
    """

    """

    __tablename__ = "attachments"

    attachment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    attachment_filename = db.Column(db.String(255), nullable=False)
    attachment_path = db.Column(db.Text, nullable=True)
    attachment_size = db.Column(db.Integer)
    ticket_id = db.Column(db.ForeignKey('tickets.ticket_id'))
    author_id = db.Column(db.ForeignKey('users.user_id'))

    ticket = db.relationship('Ticket', back_populates='attachments')
    author = db.relationship('User')