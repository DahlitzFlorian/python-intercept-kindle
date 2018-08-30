from bs4 import BeautifulSoup
import requests
import feedparser


def get_posts():
    """
    Returns a dict containing the latest medium posts of the specified user
    """
    page = requests.get("https://theintercept.com/feed/?lang=en")
    rss = feedparser.parse(page.content)

    articles = []
    for entry in rss.entries:
        soup = BeautifulSoup(entry.summary, "html.parser")
        
        new_article = {}
        new_article["title"] = entry.title
        new_article["author"] = entry.author
        new_article["tags"] = entry.tags
        new_article["published"] = entry.published
        new_article["content"] = entry.content[0].value

        new_article["filename"] = "IC - " + entry.title + ".html"

        articles.append(new_article)
    
    return articles
