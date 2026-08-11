from app import db
from app.models.base_entity import BaseEntity

class Category(BaseEntity, db.Model):
    """

    """

    __tablename__ = "categories"

    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(127), unique=True, nullable=False, index=True)
    category_description = db.Column(db.Text)

    tickets = db.relationship('Ticket', back_populates='category')
    knowledge_articles = db.relationship('KnowledgeArticle', back_populates='category')




