from app import db
from app.models.base_entity import BaseEntity

class Intervention(BaseEntity, db.Model):
    """

    """
    __tablename__ = 'interventions'

    intervention_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    intervention_date = db.Column(db.DateTime(timezone=True), nullable = False)
    intervention_duration = db.Column(db.Integer,default=0)
    intervention_report = db.Column(db.Text)

    ticket_id = db.Column(db.ForeignKey('tickets.ticket_id'), nullable=False)
    technician_id = db.Column(db.ForeignKey('users.user_id'), nullable=False)
    interventiontype_id = db.Column(db.ForeignKey('interventiontypes.interventiontype_id'), nullable=False)

    ticket = db.relationship("Ticket", back_populates='interventions')
    technician = db.relationship("User", back_populates='interventions')
    interventiontype = db.relationship("InterventionType", back_populates='interventions')

