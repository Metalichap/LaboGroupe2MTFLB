from app import db
from app.models.base_entity import BaseEntity



class Equipment(BaseEntity, db.Model):
    """

    """
    __tablename__ = "equipments"

    equipment_id = db.Column(db.Integer, primary_key=True)
    equipment_name = db.Column(db.String(255))
    equipment_type = db.Column(db.String(127))
    equipment_serial = db.Column(db.String(127), unique=True, nullable=False, index=True)
    equipment_purchase_date = db.Column(db.DateTime(timezone=True), nullable=True)

    site_id = db.Column(db.ForeignKey('sites.site_id'), nullable=False)
    user_id = db.Column(db.ForeignKey('users.user_id'), nullable=True)

    site = db.relationship('Site', back_populates='equipments')
    tickets = db.relationship('Ticket', back_populates="equipments")
    user = db.relationship('User', back_populates="equipments")

