from dataclasses import dataclass
from datetime import datetime

from ...extensions import db, ma


@dataclass
class View(db.Model):
    """This model describes an instance of an article being read."""

    __tablename__ = "views"
    id: int = db.Column(db.Integer, primary_key=True)
    author_id: int = db.Column(db.Integer, db.ForeignKey("authors.id"))
    article_id: int = db.Column(db.Integer, db.ForeignKey("articles.id"))
    date: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    author = db.relationship("Author", backref="views")
    article = db.relationship("Article", backref="views")
    

class AuthorViewSchema(ma.Schema):
    """Show all the view information."""

    class Meta:
        """The fields to display."""

        fields = ("article", "date")
        

class ArticleViewSchema(ma.Schema):
    """Show all the view information."""

    class Meta:
        """The fields to display."""

        fields = ("author", "date")
        
author_view_schema = AuthorViewSchema()
authors_views_schema = AuthorViewSchema(many=True)

article_view_schema = ArticleViewSchema()
articles_views_schema = ArticleViewSchema(many=True)