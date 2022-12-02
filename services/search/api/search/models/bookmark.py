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
