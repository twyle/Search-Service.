from ...extensions.extensions import db, ma, es
import os
from ..models.article import Article, articles_schema
from typing import List
from flask import jsonify

MAX_SIZE = 15

def all_cars(query: str):
    tokens = query.split(" ")

    clauses = [
        {
            "span_multi": {
                "match": {"fuzzy": {"name": {"value": i, "fuzziness": "AUTO"}}}
            }
        }
        for i in tokens
    ]

    payload = {
        "bool": {
            "must": [{"span_near": {"clauses": clauses, "slop": 0, "in_order": False}}]
        }
    } 

    resp = es.search(index="cars", query=payload, size=MAX_SIZE)
    return [result['_source']['name'] for result in resp['hits']['hits']]


def own_articles(query: str, articles_id: List[int]) -> List[str]:
    """Search through the articles written by this author.
    
    Searches through elasticsearch but only for articles
    written by this author.
    
    Parameters
    ----------
    query: str
        The query to search for in elasticsearch
    articles_id: List[int]
        The ids of articles written by this author
        
    Returns
    -------
    List[str]:
        A list of the articles meeting the query
    """
    payload = {
        "query": {
            "bool": {
            "should": [
                {
                "match": {
                    "title" : {
                    "query" :  query,
                    "fuzziness": "AUTO"
                    }
                }
                },
                {
                "match": {
                    "text" : {
                    "query" :  query,
                    "fuzziness": "AUTO"
                    }
                }
                }
            ],
            "filter": [
                {
                    "terms": {
                        "_id": articles_id
                    }
                }
            ]
            }
        }
        }
    resp = es.search(index="articles", body=payload, size=MAX_SIZE)
    return [result['_source'] for result in resp['hits']['hits']]


def get_own_articles_ids(author_id: int) -> List[int]:
    """Search for authors article ids.
    
    Parameters
    ----------
    author_id: int
        The authors id
        
    Returns
    -------
    list[int]:
        List of author's article ids
    """
    articles = Article.query.filter_by(author_id=author_id).all()
    return [article.id for article in articles]
    
    
def search_own_articles_es(author_id: int, query: str) -> List[str]:
    article_ids = get_own_articles_ids(author_id)
    articles = own_articles(query, article_ids)
    
    return jsonify(articles)