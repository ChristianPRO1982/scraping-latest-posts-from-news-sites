import scrapy


class LarevueiaSpider(scrapy.Spider):
    name = "larevueia"
    allowed_domains = ["larevueia.fr"]
    start_urls = [
        "https://larevueia.fr/ethique/",
        "https://larevueia.fr/nlp/",
        "https://larevueia.fr/evenements/",
        "https://larevueia.fr/ml-dl/",
        "https://larevueia.fr/data-science/",
        "https://larevueia.fr/vision/",
    ]

    def parse(self, response):
        for article in response.css('a[rel="bookmark"]'):
            url = article.css('::attr(href)').get()
            yield {
            'url': url,
            'title': article.css('::text').get()
            }


# cursor.execute("""
# CREATE TABLE IF NOT EXISTS podcasts (
# ID INTEGER PRIMARY KEY AUTOINCREMENT,
# category TEXT NOT NULL,
# podcast_name TEXT NOT NULL,
# rss_feed TEXT NOT NULL,
# title TEXT NOT NULL,
# link TEXT NOT NULL UNIQUE,
# published TEXT NOT NULL,
# description TEXT NOT NULL,
# downloaded INTEGER DEFAULT 0,
# processed INTEGER DEFAULT 0
# )""")