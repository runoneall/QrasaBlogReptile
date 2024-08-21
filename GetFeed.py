# Get Rss Feed And Change To Dict

import feedparser
import WebSend

def Get(FeedUrl:str) -> dict:
    FeedXml = WebSend.Send(FeedUrl)
    RssDoc = feedparser.parse(FeedXml)
    return dict(RssDoc)