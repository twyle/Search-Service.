from ...helpers.http_status_codes import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST
)
from flask import jsonify
from ..queries.all_cars import (
    all_cars
)
from ..queries import (
    search_own_articles_es,
    search_all_articles_es,
    search_bookmarked_articles_es,
    search_viewed_articles_es,
    search_liked_articles_es
)
import requests
import os


def verify_author(author_id: str):
    """Verify that the author exists"""
    params = {'id': author_id}
    blog_service_url = f'{os.environ["BLOG_HOST"]}/author/verify_author'
    res = requests.get(blog_service_url, params=params)
    return res.json()['author exists']


def search_all_articles(author_id: str, query: dict):
    """Search for article in all articles"""
    if not author_id:
        raise ValueError('The author id has to be provided')
    if not query:
        raise ValueError('The query string must not be empty!')
    if not isinstance(author_id, str):
        raise TypeError('The author id has to b a string')
    if not verify_author(author_id):
        raise ValueError(f'The author with id {author_id} does not exist!')
    if not isinstance(query, dict):
        raise TypeError('The query has to be a dictionary')
    if 'query' not in query.keys():
        raise ValueError('The query key is misiing!')
    if not query['query']:
        raise ValueError('The query cannot be empty!')
    if not isinstance(query['query'], str):
        raise TypeError('The query has to be a string!')
    valid_keys = ['query']
    for key in query:
        if key not in valid_keys:
            raise ValueError(f'Illegal key {key}. The only keys allwed are {valid_keys}')
    if len(query['query']) < 2:
        raise ValueError('The query has to be longer than 2 characters') 
    return search_all_articles_es(query['query']), HTTP_200_OK


def handle_search_all_articles(author_id: str, query: dict):
    """Search for article in all the articlse"""
    try:
        articles = search_all_articles(author_id, query)
    except (ValueError, TypeError) as e:
        return jsonify({'Error': str(e)}), HTTP_400_BAD_REQUEST
    else:
        return articles
    
    
def search_own_articles(author_id: str, query: dict):
    """Search for article in own articles"""
    if not author_id:
        raise ValueError('The author id has to be provided')
    if not query:
        raise ValueError('The query string must not be empty!')
    if not isinstance(author_id, str):
        raise TypeError('The author id has to b a string')
    if not verify_author(author_id):
        raise ValueError(f'The author with id {author_id} does not exist!')
    if not isinstance(query, dict):
        raise TypeError('The query has to be a dictionary')
    if 'query' not in query.keys():
        raise ValueError('The query key is misiing!')
    if not query['query']:
        raise ValueError('The query cannot be empty!')
    if not isinstance(query['query'], str):
        raise TypeError('The query has to be a string!')
    valid_keys = ['query']
    for key in query:
        if key not in valid_keys:
            raise ValueError(f'Illegal key {key}. The only keys allwed are {valid_keys}')
    if len(query['query']) < 2:
        raise ValueError('The query has to be longer than 2 characters')
    print(query['query'])
    return search_own_articles_es(int(author_id), query['query']), HTTP_200_OK


def handle_search_own_articles(author_id: str, query: dict):
    """Search for article in all the articlse"""
    try:
        articles = search_own_articles(author_id, query)
    except (ValueError, TypeError) as e:
        return jsonify({'Error': str(e)}), HTTP_400_BAD_REQUEST
    else:
        return articles


def search_bookmarked_articles(author_id: str, query: dict):
    """Search for article in own articles"""
    if not author_id:
        raise ValueError('The author id has to be provided')
    if not query:
        raise ValueError('The query string must not be empty!')
    if not isinstance(author_id, str):
        raise TypeError('The author id has to b a string')
    if not verify_author(author_id):
        raise ValueError(f'The author with id {author_id} does not exist!')
    if not isinstance(query, dict):
        raise TypeError('The query has to be a dictionary')
    if 'query' not in query.keys():
        raise ValueError('The query key is misiing!')
    if not query['query']:
        raise ValueError('The query cannot be empty!')
    if not isinstance(query['query'], str):
        raise TypeError('The query has to be a string!')
    valid_keys = ['query']
    for key in query:
        if key not in valid_keys:
            raise ValueError(f'Illegal key {key}. The only keys allwed are {valid_keys}')
    if len(query['query']) < 2:
        raise ValueError('The query has to be longer than 2 characters')
    print(query['query'])
    return search_bookmarked_articles_es(int(author_id), query['query']), HTTP_200_OK


def handle_search_bookmarked_articles(author_id: str, query: dict):
    """Search for article in bookmarked articlse"""
    try:
        articles = search_bookmarked_articles(author_id, query)
    except (ValueError, TypeError) as e:
        return jsonify({'Error': str(e)}), HTTP_400_BAD_REQUEST
    else:
        return articles


def search_viewed_articles(author_id: str, query: dict):
    """Search for article in viewed articles"""
    if not author_id:
        raise ValueError('The author id has to be provided')
    if not query:
        raise ValueError('The query string must not be empty!')
    if not isinstance(author_id, str):
        raise TypeError('The author id has to b a string')
    if not verify_author(author_id):
        raise ValueError(f'The author with id {author_id} does not exist!')
    if not isinstance(query, dict):
        raise TypeError('The query has to be a dictionary')
    if 'query' not in query.keys():
        raise ValueError('The query key is misiing!')
    if not query['query']:
        raise ValueError('The query cannot be empty!')
    if not isinstance(query['query'], str):
        raise TypeError('The query has to be a string!')
    valid_keys = ['query']
    for key in query:
        if key not in valid_keys:
            raise ValueError(f'Illegal key {key}. The only keys allwed are {valid_keys}')
    if len(query['query']) < 2:
        raise ValueError('The query has to be longer than 2 characters')
    print(query['query'])
    return search_viewed_articles_es(int(author_id), query['query']), HTTP_200_OK


def handle_search_viewed_articles(author_id: str, query: dict):
    """Search for article in viewed articlse"""
    try:
        articles = search_viewed_articles(author_id, query)
    except (ValueError, TypeError) as e:
        return jsonify({'Error': str(e)}), HTTP_400_BAD_REQUEST
    else:
        return articles
    
def search_liked_articles(author_id: str, query: dict):
    """Search for article in liked articles"""
    if not author_id:
        raise ValueError('The author id has to be provided')
    if not query:
        raise ValueError('The query string must not be empty!')
    if not isinstance(author_id, str):
        raise TypeError('The author id has to b a string')
    if not verify_author(author_id):
        raise ValueError(f'The author with id {author_id} does not exist!')
    if not isinstance(query, dict):
        raise TypeError('The query has to be a dictionary')
    if 'query' not in query.keys():
        raise ValueError('The query key is misiing!')
    if not query['query']:
        raise ValueError('The query cannot be empty!')
    if not isinstance(query['query'], str):
        raise TypeError('The query has to be a string!')
    valid_keys = ['query']
    for key in query:
        if key not in valid_keys:
            raise ValueError(f'Illegal key {key}. The only keys allwed are {valid_keys}')
    if len(query['query']) < 2:
        raise ValueError('The query has to be longer than 2 characters')
    print(query['query'])
    return search_liked_articles_es(int(author_id), query['query']), HTTP_200_OK


def handle_search_liked_articles(author_id: str, query: dict):
    """Search for article in liked articlse"""
    try:
        articles = search_liked_articles(author_id, query)
    except (ValueError, TypeError) as e:
        return jsonify({'Error': str(e)}), HTTP_400_BAD_REQUEST
    else:
        return articles