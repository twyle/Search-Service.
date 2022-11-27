import os
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    """Base configuration."""

    DEBUG = True
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")

    ES_HOST = os.environ["ES_HOST"]
    ES_PORT = os.environ['ES_PORT']

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    JWT_SECRET_KEY = "super-secret-key"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        hours=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", "24"))
    )
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(
        days=int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES", "7"))
    )


class DevelopmentConfig(BaseConfig):
    """Development confuguration."""

    ES_HOST = os.environ["ES_HOST"]
    ES_PORT = os.environ['ES_PORT']

    JWT_SECRET_KEY = "super-secret-key"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        hours=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", "24"))
    )
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(
        days=int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES", "7"))
    )


class TestingConfig(BaseConfig):
    """Testing configuration."""

    TESTING = True
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    
    ES_HOST = os.environ["ES_HOST"]
    ES_PORT = os.environ['ES_PORT']

    JWT_SECRET_KEY = "super-secret-key"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        hours=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", "24"))
    )
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(
        days=int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES", "7"))
    )


class ProductionConfig(BaseConfig):
    """Production configuration."""

    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    
    ES_HOST = os.environ["ES_HOST"]
    ES_PORT = os.environ['ES_PORT']

    JWT_SECRET_KEY = "super-secret-key"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        hours=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", "24"))
    )
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(
        days=int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES", "7"))
    )


Config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "staging": ProductionConfig,
}
