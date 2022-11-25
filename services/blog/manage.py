from flask.cli import FlaskGroup
from api.extensions.extensions import init_celery, celery
from api import create_app, db

app = create_app()
cli = FlaskGroup(create_app=create_app)
init_celery(celery, app)


@cli.command("create_db")
def create_db():
    """Create the database and all the tables."""
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    cli()
