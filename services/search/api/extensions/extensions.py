from dotenv import load_dotenv
from flasgger import LazyString, Swagger
from flask import request
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from elasticsearch import Elasticsearch
import os
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


load_dotenv()

cors = CORS()
jwt = JWTManager()
db = SQLAlchemy()
ma = Marshmallow()


def create_es_client():
    """Create the es client."""
    if os.environ['FLASK_ENV'] == 'development':
        ES_HOST = os.environ["ES_HOST"]
        ES_PORT = os.environ['ES_PORT']
        es = Elasticsearch(hosts=[f"{ES_HOST}:{ES_PORT}"])
        return es
    elif os.environ['FLASK_ENV'] in ['production', 'staging']:
        CLOUD_ID = os.environ['ES_CLOUD_ID']
        ES_USER = os.environ['ES_USER']
        ES_PASSWORD = os.environ['ES_PASSWORD']
        es = Elasticsearch(
            cloud_id=CLOUD_ID,
            basic_auth=(ES_USER, ES_PASSWORD)
        )
        return es

es = create_es_client()

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Article Search App.",
        "description": "An application for searching for articles.",
        "contact": {
            "responsibleOrganization": "",
            "responsibleDeveloper": "",
            "email": "lyceokoth@gmail.com",
            "url": "www.twitter.com/lylethedesigner",
        },
        "termsOfService": "www.twitter.com/deve",
        "version": "1.0",
    },
    "host": LazyString(lambda: request.host),
    "basePath": "/",  # base bash for blueprint registration
    "schemes": ["http", "https"],
    "securityDefinitions": {
        "APIKeyHeader": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": 'JWT Authorization header using the Bearer scheme. Example:"Authorization: Bearer {token}"',
        }
    },
}


swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/",
}

swagger = Swagger(template=swagger_template, config=swagger_config)
