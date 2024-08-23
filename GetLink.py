import GetAllBlog

def Get(Title:str) -> str:
    AllBlog = GetAllBlog.Get()

    for BlogInfo in AllBlog:
        BlogTitle = BlogInfo['title']
        if BlogTitle == Title:
            BlogLink = BlogInfo['link']
            return BlogLink