import json

with open('./data/News_Category_Dataset.json') as news_dataset:
  newsList = [json.loads(article) for article in news_dataset]
