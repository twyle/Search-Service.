from dataclasses import dataclass
from datetime import datetime
import json
from ...extensions import db, ma


@dataclass
class Like(db.Model):
    """The Like Model."""

    __tablename__ = "likes"
    id: int = db.Column(db.Integer, primary_key=True)
    author_id: int = db.Column(db.Integer, db.ForeignKey("authors.id"))
    article_id: int = db.Column(db.Integer, db.ForeignKey("articles.id"))
    date: datetime = db.Column(db.DateTime, default=datetime.utcnow)


class AuthorLikeSchema(ma.Schema):
    """Show all the like information."""

    class Meta:
        """The fields to display."""

        fields = (
            "article",
            "date"
        )
        

class ArticleLikeSchema(ma.Schema):
    """Show all the like information."""

    class Meta:
        """The fields to display."""

        fields = (
            "author",
            "date"
        )


author_like_schema = AuthorLikeSchema()
author_likes_schema = AuthorLikeSchema(many=True)

article_like_schema = ArticleLikeSchema()
article_likes_schema = ArticleLikeSchema(many=True)
