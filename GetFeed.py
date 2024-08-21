import feedparser
import WebSend

def Get(FeedUrl:str):
    FeedXml = WebSend.Send(FeedUrl)
    RssDoc = feedparser.parse(FeedXml)
    return dict(RssDoc)