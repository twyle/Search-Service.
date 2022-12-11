import os

from flasgger import LazyJSONEncoder
from sqlalchemy_utils import database_exists
from ..search.views import search
from elasticsearch import Elasticsearch
from elastic_transport import ConnectionError

from ..extensions import cors, jwt, swagger, db, ma, es
from ..config.logger import app_logger
import requests


def register_extensions(app):
    """Register the app extensions."""
    app.json_encoder = LazyJSONEncoder
    cors.init_app(app)
    swagger.init_app(app)
    jwt.init_app(app)
    db.init_app(app)
    ma.init_app(app)


def register_blueprints(app):
    app.register_blueprint(search, url_prefix="/search")


def create_db_conn_string() -> str:
    """Create the database connection string.

    Creates the database connection string for a given flask environment.

    Returns
    -------
    db_connection_string: str
        The database connection string
    """

    POSTGRES_HOST = os.environ["POSTGRES_HOST"]
    POSTGRES_PORT = os.environ["POSTGRES_PORT"]
    POSTGRES_USER = os.environ["POSTGRES_USER"]
    POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
    POSTGRES_DB = os.environ["POSTGRES_DB"]

    return f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


def check_if_database_exists(db_connection_string: str) -> bool:
    """Check if database exists.

    Ensures that the database exists before starting the application.

    Attributes
    ----------
    db_connection: str
        The database URL

    Raises
    ------
    ValueError:
        If the db_connection_string is empty or is not a string.

    Returns
    -------
    db_exists: bool
        True if database exists or False if it does not
    """
    if not db_connection_string:
        raise ValueError("The db_connection_string cannot be a null value.")

    if not isinstance(db_connection_string, str):
        raise ValueError("The db_connection_string has to be string")
    
    if not database_exists(db_connection_string):
        raise ValueError("The Postgres database is not connected")
    
    try:  
        es.info()
    except Exception as e:
        app_logger.critical('Could not connect to ES cluster!')
        return False
    else:
        app_logger.info(f"Connected to ElasticSearch cluster `{es.info().body['cluster_name']}`")
        return True
    
    
def blog_service_up():
    """Ceh ifblog service is up""" 
    try:
        res = requests.get(f'{os.environ["BLOG_HOST"]}/')
    except Exception:
        raise ValueError('Unable to connect to the blog service')
    else:
        return res.ok


def check_configuration():
    """Check if all the configs are set."""
    # Check database connection
    if not check_if_database_exists(create_db_conn_string()):
        raise ValueError("The database is not connected!")
    if not blog_service_up():
        raise ValueError('The blog service is not running!')
