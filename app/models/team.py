from app import db
from app.models.base_entity import BaseEntity

class Team(BaseEntity, db.Model):
    """

    """

    __tablename__ = "teams"

    team_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_name = db.Column(db.String(127), unique=True, nullable=False, index=True)
    team_description = db.Column(db.Text)

    members = db.relationship('User', back_populates='team')
