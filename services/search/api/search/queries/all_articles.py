from ...extensions.extensions import db, ma, es
import os
from ..models.article import Article, articles_schema
from typing import List
from flask import jsonify

MAX_SIZE = 15


def all_articles(query: str) -> List[str]:
    """Search through the all articles.
    
    Parameters
    ----------
    query: str
        The query to search for in elasticsearch
        
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
            ]
            }
        }
        }
    resp = es.search(index=os.environ['ES_INDEX'], body=payload, size=MAX_SIZE)
    return [result['_source'] for result in resp['hits']['hits']]
    
    
def search_all_articles_es(query: str) -> List[str]:
    articles = all_articles(query)
    
    return jsonify(articles)