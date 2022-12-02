import json

def create_articles():
    articles = []
    with open('News_Category_Dataset_v3.json', 'r') as f:
        lines = f.readlines()
        for line in lines:
            article = {}
            data = json.loads(line)
            article['title'] = data['headline']
            article['category'] = data['category'].lower()
            article['text'] = data['short_description']
            article['date'] = data['date']
            
            articles.append(article)

    with open('articles.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)
    
if __name__ == '__main__':
    create_articles()