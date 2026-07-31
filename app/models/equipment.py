from app import db
from app.models.base_entity import BaseEntity



class Equipment(BaseEntity, db.Model):
    """

    """

    equipment_id = db.Column(db.Integer, primary_key=True)

    site_id = db.Column(db.ForeignKey('sites.site_id'), nullable=False)

    site = db.relationship('Site', back_populates='equipments')



