from app import db
from app.models.base_entity import BaseEntity


class Site(BaseEntity, db.Model):
    """

    """

    __tablename__ = "sites"

    site_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    site_name = db.Column(db.String(127), unique=True, nullable=False, index=True)
    site_address = db.Column(db.String(255))
    site_city = db.Column(db.String(63))

    users = db.relationship('User', back_populates='site')
    equipments = db.relationship('Equipment', back_populates='site')
