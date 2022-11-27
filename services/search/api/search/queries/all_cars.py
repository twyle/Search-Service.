from ...extensions.extensions import es

MAX_SIZE = 15

def all_cars(query: str):
    tokens = query.split(" ")

    clauses = [
        {
            "span_multi": {
                "match": {"fuzzy": {"name": {"value": i, "fuzziness": "AUTO"}}}
            }
        }
        for i in tokens
    ]

    payload = {
        "bool": {
            "must": [{"span_near": {"clauses": clauses, "slop": 0, "in_order": False}}]
        }
    }

    resp = es.search(index="cars", query=payload, size=MAX_SIZE)
    return [result['_source']['name'] for result in resp['hits']['hits']]