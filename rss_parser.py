import json
import feedparser

rss_feeds = [
    "http://rss.cnn.com/rss/cnn_topstories.rss",
    "http://qz.com/feed",
    "http://feeds.foxnews.com/foxnews/politics",
    "http://feeds.reuters.com/reuters/businessNews",
    "http://feeds.feedburner.com/NewshourWorld",
    "https://feeds.bbci.co.uk/news/world/asia/india/rss.xml"
]

def parse_rss(feed_url):
    parsed_feed = feedparser.parse(feed_url)
    articles = []
    for entry in parsed_feed.entries:
        article = {
            "title": entry.title,
            "content": entry.summary,
            "pub_date": entry.published,
            "url": entry.link
        }
        articles.append(article)
    return articles

all_articles = []
for feed_url in rss_feeds:
    all_articles.extend(parse_rss(feed_url))

with open('articles.json', 'w') as json_file:
    json.dump(all_articles, json_file)
