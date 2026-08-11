from app import db
from app.models.base_entity import BaseEntity

class InterventionType(BaseEntity, db.Model):
    """

    """
    __tablename__ = 'interventiontypes'

    interventiontype_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    interventiontype_name = db.Column(db.String(127), unique=True, nullable=False)
    interventiontype_description = db.Column(db.Text)

    interventions = db.relationship("Intervention", back_populates='interventiontype')

