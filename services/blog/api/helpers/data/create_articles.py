import csv
import json

with open('Articles.csv', errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    articles = []
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            article = {
                'title': row[2],
                'text': row[0],
                'date': row[1],
                'tags': [row[3]]
            }
            articles.append(article)
            line_count += 1
    with open('articles.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)