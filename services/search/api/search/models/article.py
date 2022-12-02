import os
from dataclasses import dataclass
from datetime import datetime

from flask import current_app
from sqlalchemy.dialects.postgresql import ARRAY

from ...extensions import db, ma


@dataclass
class Article(db.Model):
    """The article class"""

    __tablename__ = "articles"

    id: int = db.Column(db.Integer, primary_key=True)
    author_id: int = db.Column(db.Integer, db.ForeignKey("authors.id"))
    title: str = db.Column(db.Text, nullable=False)
    text: str = db.Column(db.Text, nullable=False)
    image: str = db.Column(db.String(100), nullable=True)
    date_published: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    date_edited: datetime = db.Column(db.DateTime, nullable=True)
    tag = db.Column(db.String(100), nullable=True)

    @staticmethod
    def article_with_id_exists(article_id):
        """Check if article with given id exists."""
        if Article.query.filter_by(id=article_id).first():
            return True
        return False


    @staticmethod
    def get_article(article_id: int):
        """Get an article."""
        article = Article.query.filter_by(id=article_id).first()
        return article

    @staticmethod
    def all_articles(author_id=None):
        """List all users."""
        if author_id:
            return Article.query.filter_by(author_id=author_id)
        return Article.query.all()



class ArticleSchema(ma.Schema):
    """Show all the article information."""

    class Meta:
        """The fields to display."""

        fields = ("id", "author_id", "title", "text", "image", "date_published", "date_edited", "tag")
        

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)
