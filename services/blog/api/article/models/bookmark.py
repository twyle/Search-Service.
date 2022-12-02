from dataclasses import dataclass
from datetime import datetime
import json
from ...extensions import db, ma


@dataclass
class Bookmark(db.Model):
    """The Bookmark Model."""

    __tablename__ = "bookmarks"

    id: int = db.Column(db.Integer, primary_key=True)
    author_id: int = db.Column(db.Integer, db.ForeignKey("authors.id"))
    article_id: int = db.Column(db.Integer, db.ForeignKey("articles.id"))
    date: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    author = db.relationship("Author", backref="bookmarks")
    article = db.relationship("Article", backref="bookmarks")
    
    def __repr__(self) -> str:
        data = json.dumps({
            'author_id': self.author_id,
            'date': str(self.date)
        })
        return data


class ArticleBookmarkSchema(ma.Schema):
    """Show all the article information."""

    class Meta:
        """The fields to display."""

        fields = (
            "author",
            "date",
        )
        
        
class AuthorBookmarkSchema(ma.Schema):
    """Show all the article information."""

    class Meta:
        """The fields to display."""

        fields = ("article", "date")
        
author_bookmark_schema = AuthorBookmarkSchema()
author_bookmarks_schema = AuthorBookmarkSchema(many=True)


article_bookmark_schema = ArticleBookmarkSchema()
article_bookmarks_schema = ArticleBookmarkSchema(many=True)
