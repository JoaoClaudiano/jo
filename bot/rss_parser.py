import feedparser

RSS_FEED = "https://g1.globo.com/rss/g1/ultimas-noticias.rss"

def fetch_news():
    feed = feedparser.parse(RSS_FEED)
    news_items = []
    for entry in feed.entries[:5]:  # últimas 5 notícias
        news_items.append({
            "title": entry.title,
            "summary": getattr(entry, "summary", ""),
            "link": entry.link
        })
    return news_items