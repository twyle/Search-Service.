import json
import random
from faker import Faker
from ...extensions.extensions import es


def create_index(index_name: str):
    """Create the ES index"""
    mapping = {
    "settings": {
        "number_of_shards": 2,
        "number_of_replicas": 1
    },
    "mappings": {
        "properties": {
            "title": {
                "type": "text" 
            },
            "text": {
                "type": "text"
            },
            "category": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "date": {
                "type": "date",
                "format":"yyyy-MM-dd"
            }
        }
    }
    }

    print("creating 'example_index' index...")
    es.indices.create(index = index_name, body = mapping)


def load_authors(file_path):
    """Create the authors"""
    data = None
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def load_articles(file_path):
    """Create the authors"""
    data = None
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def generate_views(articles, authors):
    """Generate views for the articles."""
    article_views = []
    for article in articles:
        views = random.randint(1,10)
        for _ in range(views):
            author = random.choice(authors)
            article = random.choice(articles)
            article_views.append({
                'author': author,
                'article': article
            })
    return article_views


def generate_likes(articles, authors):
    """Generate likes for the articles."""
    article_likes = []
    for article in articles:
        likes = random.randint(1,10)
        for _ in range(likes):
            author = random.choice(authors)
            article = random.choice(articles)
            article_likes.append({
                'author': author,
                'article': article
            })
    return article_likes


def generate_bookmarks(articles, authors):
    """Generate bookmarks for the articles."""
    article_bookmarks = []
    for article in articles:
        bookmarks = random.randint(1,10)
        for _ in range(bookmarks):
            author = random.choice(authors)
            article = random.choice(articles)
            article_bookmarks.append({
                'author': author,
                'article': article
            })
    return article_bookmarks


def generate_comments(articles, authors):
    """Generate comments for the articles."""
    fake = Faker()
    article_comments = []
    for article in articles:
        comments = random.randint(1,10)
        for _ in range(comments):
            author = random.choice(authors)
            article = random.choice(articles)
            article_comments.append({
                'author': author,
                'article': article,
                'comment': fake.text().replace('/n', '')
            })
    return article_comments


if __name__ == '__main__':
    articles = load_articles('./articles.json')
    print(articles)