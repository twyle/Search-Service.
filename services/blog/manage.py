from flask.cli import FlaskGroup
from api.extensions.extensions import init_celery, celery, es
from api import create_app, db
from api.helpers.data.create_data import load_authors, load_articles
from api.author.models.author import Author
from api.article.models.article import Article, es_schema
import random
from datetime import datetime
import os


app = create_app()
cli = FlaskGroup(create_app=create_app)
init_celery(celery, app)


@cli.command("create_db")
def create_db():
    """Create the database and all the tables."""
    db.drop_all()
    db.create_all()
    db.session.commit()
    

@cli.command("seed_db")
def seed_db():
    """Create the data."""
    authors_data = load_authors('./api/helpers/data/authors.json')
    articles_data = load_articles('./api/helpers/data/articles.json')
    for author_data in authors_data:
        author = Author(
            name=author_data['name'],
            email_address=author_data['email_address']
        )
        db.session.add(author)
    db.session.commit()
    authors = Author.query.all()
    for article_data in articles_data:
        author = random.choice(authors)
        article = Article(
            title=article_data['title'],
            text=article_data['text'],
            author=author,
            date_published=datetime.strptime(article_data['date'], "%m/%d/%Y").date(),
            tags=[tag for tag in article_data['tags']]
        )
        db.session.add(article)
    db.session.commit()
    articles = Article.query.all()
    es.indices.delete(index=os.environ['ES_INDEX'], ignore=[400, 404])
    for article in articles:
        document = es_schema.dump(article)
        es.index(index=os.environ['ES_INDEX'], document=document)
        

if __name__ == "__main__":
    cli()
