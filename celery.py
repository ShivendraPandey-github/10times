from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def process_news(article):
    
    pass
