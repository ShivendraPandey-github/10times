from celery import Celery
from models import NewsArticle
import json
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



engine = create_engine('postgresql://root:12345678@localhost:5432')

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def process_news(article):
   
    pass

with open('articles.json', 'r') as json_file:
    all_articles = json.load(json_file)

Session = sessionmaker(bind=engine)
session = Session()

for article in all_articles:
    db_article = NewsArticle(**article, category=None)
    session.merge(db_article)

session.commit()
session.close()
