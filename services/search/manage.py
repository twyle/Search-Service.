from flask.cli import FlaskGroup
from api import create_app
from api.extensions.extensions import es

app = create_app()
cli = FlaskGroup(create_app=create_app)


def create_index():
    """Create the ES index"""
    request_body = {
        "settings" : {
            "number_of_shards": 5,
            "number_of_replicas": 1
        },

        'mappings': {
            'examplecase': {
                'properties': {
                    'address': {'index': 'not_analyzed', 'type': 'string'},
                    'date_of_birth': {'index': 'not_analyzed', 'format': 'dateOptionalTime', 'type': 'date'},
                    'some_PK': {'index': 'not_analyzed', 'type': 'string'},
                    'fave_colour': {'index': 'analyzed', 'type': 'string'},
                    'email_domain': {'index': 'not_analyzed', 'type': 'string'},
                }}}
    }
    print("creating 'example_index' index...")
    es.indices.create(index = 'example_index', body = request_body)    


if __name__ == "__main__":
    cli()
