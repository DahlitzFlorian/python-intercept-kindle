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


def create_files(articles: list):
    for article in articles:
        with open(article["filename"], "wb") as f:
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
