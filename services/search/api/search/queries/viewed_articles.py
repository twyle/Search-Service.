from ...extensions.extensions import db, ma, es
import os
from ..models.views import View
from typing import List
from flask import jsonify

MAX_SIZE = 15


def viewed_articles(query: str, articles_id: List[int]) -> List[str]:
    """Search through the articles viewed by this author.
    
    Searches through elasticsearch but only for articles
    viewed by this author.
    
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
    resp = es.search(index=os.environ['ES_INDEX'], body=payload, size=MAX_SIZE)
    return [result['_source'] for result in resp['hits']['hits']]


def get_viewed_articles_ids(author_id: int) -> List[int]:
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
    views = View.query.filter_by(author_id=author_id).all()
    return [view.article_id for view in views]
    
    
def search_viewed_articles_es(author_id: int, query: str) -> List[str]:
    article_ids = get_viewed_articles_ids(author_id)
    articles = viewed_articles(query, article_ids)
    
    return jsonify(articles)