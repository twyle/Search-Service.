import os

import boto3
from dotenv import load_dotenv
from flasgger import LazyString, Swagger
from flask import request
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from celery import Celery


load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
cors = CORS()
jwt = JWTManager()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.environ["AWS_ACCESS_KEY"],
    aws_secret_access_key=os.environ["AWS_ACCESS_SECRET"],
)

def make_celery():
    """Create the celery extension."""
    celery = Celery(__name__)
    return celery


def init_celery(celery, app):
    """Initialize the celery extension."""
    celery.conf.update(app.config)

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask


celery = make_celery()

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Article Publishing App.",
        "description": "An application for creating and publishing articles.",
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
