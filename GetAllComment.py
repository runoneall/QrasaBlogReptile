import GetAllBlog
import GetComment

def Get() -> list[dict]:
    print('Process Rss')
    AllBlog = GetAllBlog.Get()

    CommentList = list()
    for BlogInfo in AllBlog:
        BlogTitle = BlogInfo['title']
        BlogLink = BlogInfo['link']

        print('Process', BlogTitle)
        Comments = GetComment.Get(BlogLink)
        CommentList.append({BlogTitle: Comments})

    return CommentList