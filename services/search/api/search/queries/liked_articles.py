from ...extensions.extensions import db, ma, es
import os
from ..models.like import Like
from typing import List
from flask import jsonify

MAX_SIZE = 15


def liked_articles(query: str, articles_id: List[int]) -> List[str]:
    """Search through the articles liked by this author.
    
    Searches through elasticsearch but only for articles
    liked by this author.
    
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


def get_liked_articles_ids(author_id: int) -> List[int]:
    """Search through articles likked by this author.
    
    Parameters
    ----------
    author_id: int
        The authors id
        
    Returns
    -------
    list[int]:
        List of author's article ids
    """
    likes = Like.query.filter_by(author_id=author_id).all()
    return [like.article_id for like in likes]
    
    
def search_liked_articles_es(author_id: int, query: str) -> List[str]:
    article_ids = get_liked_articles_ids(author_id)
    articles = liked_articles(query, article_ids)
    
    return jsonify(articles)