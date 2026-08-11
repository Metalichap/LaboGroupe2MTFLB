from app import db
from app.models.base_entity import BaseEntity

class Comment(BaseEntity, db.Model):
    """

    """

    __tablename__ = "comments"
    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment_content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.ForeignKey('users.user_id'))
    ticket_id = db.Column(db.ForeignKey('tickets.ticket_id'))

    ticket = db.relationship("Ticket", back_populates="comments")
    author = db.relationship("User", back_populates="comments")

