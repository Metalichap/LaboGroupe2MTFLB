from app import db
from app.models.base_entity import BaseEntity

class KnowledgeArticle(BaseEntity, db.Model):
    """

    """

    __tablename__ = "knowledgesarticles"

    article_id = db.Column(db.Integer, primary_key=True)
    article_title = db.Column(db.String(255), nullable=False)
    article_content = db.Column(db.Text)
    category_id = db.Column(db.ForeignKey('categories.category_id'))
    author_id = db.Column(db.ForeignKey('users.user_id'))

    category = db.relationship('Category', back_populates='knowledge_articles')
    author = db.relationship('User', back_populates='knowledge_articles')


