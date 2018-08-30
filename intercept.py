import requests
import feedparser
import os
from datetime import datetime


def get_articles() -> list:
    """
    Returns a list containing the latest articles from The Intercept
    """
    page = requests.get("https://theintercept.com/feed/?lang=en")
    rss = feedparser.parse(page.content)

    articles = []
    for entry in rss.entries:
        date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S +%f")
        date = str(date.year) + str(date.month) + str(date.day)
        today = datetime.today()
        today = str(today.year) + str(today.month) + str(today.day)
        if date != today:
            continue
        
        new_article = {}
        new_article["title"] = entry.title
        new_article["author"] = entry.author
        new_article["tags"] = entry.tags
        new_article["published"] = entry.published
        new_article["content"] = entry.content[0].value

        new_article["filename"] = "IC - " + entry.title + ".html"

        articles.append(new_article)
    
    return articles


def create_files(articles: list) -> None:
    """
    Creates the HTML-files based on the list of articles and saves them
    to the file system
    """
    for article in articles:
        if not os.path.exists("tmp"):
            os.mkdir("tmp")
        
        path = "tmp\\" + article["filename"]
        with open(path, "wb") as f:
            f.write(b"<head><meta charset='utf-8'></head>")
            f.write(b"<h1>")
            f.write(article["title"].encode("utf-8"))
            f.write(b"</h1>")
            f.write(b"<div>")
            f.write(b"<b>Author:</b> ")
            f.write(article["author"].encode("utf-8"))
            f.write(b"<br>")
            f.write(b"<b>Categories:</b> ")
            for i, category in enumerate(article["tags"]):
                f.write(category.term.encode("utf-8"))
                if i != len(article["tags"]) - 1:
                    f.write(b", ")
            f.write(b"<br>")
            f.write(b"<b>Published:</b> ")
            f.write(article["published"].encode("utf-8"))
            f.write(b"</div>")
            f.write(b"<article>")
            f.write(article["content"].encode("utf-8"))
            f.write(b"</article>")
