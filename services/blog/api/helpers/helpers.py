import os

from flasgger import LazyJSONEncoder
from sqlalchemy_utils import database_exists

from ..article.views import article
from ..author import author
from ..extensions import cors, db, jwt, ma, migrate, swagger


def register_extensions(app):
    """Register the app extensions."""
    app.json_encoder = LazyJSONEncoder
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    swagger.init_app(app)
    jwt.init_app(app)


def register_blueprints(app):
    app.register_blueprint(author, url_prefix="/author")
    app.register_blueprint(article, url_prefix="/article")


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

    db_exists = database_exists(db_connection_string)

    return db_exists


def check_configuration():
    """Check if all the configs are set."""
    # Check database connection
    if not check_if_database_exists(create_db_conn_string()):
        raise ValueError("The database is not connected!")
    

def create_article_index(es, index_name='articles'):
    body = {
        "mappings":{
            "properties": {
                "title": {"type": "text", "analyzer": "english"},
                "ethnicity": {"type": "text", "analyzer": "standard"},
                "director": {"type": "text", "analyzer": "standard"},
                "cast": {"type": "text", "analyzer": "standard"},
                "genre": {"type": "text", "analyzer": "standard"},
                "plot": {"type": "text", "analyzer": "english"},
                "year": {"type": "integer"},
                "wiki_page": {"type": "keyword"}
            }
        }
    }
    response = es.indices.create(index_name, body=body)