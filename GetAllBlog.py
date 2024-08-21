# Process Rss Dict And Return

import GetFeed
import Config

def Get() -> list[dict]:
    RssDoc = GetFeed.Get(Config.BlogRssFeed)
    Posts = RssDoc['entries']

    ReturnPosts = list()
    for Post in Posts:
        OnePost = dict()
        OnePost['title'] = Post['title']
        OnePost['link'] = Post['link']
        OnePost['author'] = Post['author']
        OnePost['time'] = Post['published']
        Tags = Post['tags']
        OnePost['tags'] = list()
        for Tag in Tags:
            OneTag = dict()
            OneTag['term'] = Tag['term']
            OneTag['label'] = Tag['label']
            OnePost['tags'].append(OneTag)
        ReturnPosts.append(OnePost)

    return ReturnPosts