import json


def load_authors(file_path):
    """Create the authors"""
    data = None
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def load_articles(file_path):
    """Create the authors"""
    data = None
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data