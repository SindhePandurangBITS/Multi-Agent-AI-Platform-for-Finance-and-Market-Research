""" news scraper with newspaper3k for articles """

from newspaper import Article

def fetch_article(url):
    artcl = Article(url)
    artcl.download()
    artcl.parse()
    return artcl.text
