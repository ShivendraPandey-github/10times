from sqlalchemy import Integer, create_engine, Column, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class NewsArticle(Base):
    __tablename__ = 'news_articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    content = Column(Text)
    pub_date = Column(DateTime)
    url = Column(String(255), unique=True)
    category = Column(String(50))
