from flask.cli import FlaskGroup
from api.extensions.extensions import init_celery, celery, es
from api import create_app, db
from api.helpers.data.create_data import (
    load_authors,
    load_articles,
    generate_views,
    generate_likes,
    generate_bookmarks,
    generate_comments,
    create_index
)
from api.author.models.author import Author
from api.article.models.views import View
from api.article.models.like import Like
from api.article.models.bookmark import Bookmark
from api.article.models.comment import Comment
from api.article.models.article import Article
import random
from datetime import datetime
import os
import faker


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
    fake = faker.Faker()
    authors_data = load_authors('./api/helpers/data/authors.json')
    articles_data = load_articles('./api/helpers/data/articles.json')
    # for author_data in authors_data:
    #     author = Author(
    #         name=author_data['name'],
    #         email_address=author_data['email_address']
    #     )
    #     db.session.add(author)
    # db.session.commit()
    # authors = Author.query.all()
    # for article_data in articles_data[:10]:
    #     author = random.choice(authors)
    #     article = Article(
    #         tag=article_data['category'],
    #         title=article_data['title'],
    #         text=article_data['text'],
    #         author=author,
    #         date_published=datetime.strptime(article_data['date'], "%Y-%m-%d").date(),
    #     )
    #     db.session.add(article)
    # db.session.commit()
    # articles = Article.query.all()
    # article_views = generate_views(articles, authors)
    # for article_view in article_views:
    #     view = View(author=article_view['author'], article=article_view['article'], date=fake.date())
    #     db.session.add(view)
    # db.session.commit()
    # article_likes = generate_likes(articles, authors)
    # for article_like in article_likes:
    #     like = Like(author=article_like['author'], article=article_like['article'], date=fake.date())
    #     db.session.add(like)
    # db.session.commit()
    # article_bookmarks = generate_bookmarks(articles, authors)
    # for article_bookmark in article_bookmarks:
    #     bookmark = Bookmark(author=article_bookmark['author'], article=article_bookmark['article'], date=fake.date())
    #     db.session.add(bookmark)
    # db.session.commit()
    # article_comments = generate_comments(articles, authors)
    # for article_comment in article_comments:
    #     comment = Comment(author=article_comment['author'], 
    #                       article=article_comment['article'], 
    #                       date=fake.date(),
    #                       comment=article_comment['comment'])
    #     db.session.add(comment)
    # db.session.commit()
    es.indices.delete(index=os.environ['ES_INDEX'], ignore=[400, 404])
    create_index(os.environ['ES_INDEX'])
    for count, article in enumerate(articles_data[:100], start=1):
        es.index(index=os.environ['ES_INDEX'], body=article, id=str(count))
        

if __name__ == "__main__":
    cli()
