from faker import Faker
import json

fake = Faker()

def create_authors(num_authors):
    """Create a single author"""
    authors = []
    for _ in range(num_authors):
        author = {
            'name': fake.name(),
            'email_address': fake.email()
        }
        authors.append(author)
    with open('authors.json', 'w', encoding='utf-8') as f:
        json.dump(authors, f, ensure_ascii=False, indent=4)
    
if __name__ == '__main__':
    create_authors(20)
    