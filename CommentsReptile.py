# Get Comments And Return List

from bs4 import BeautifulSoup
import GetAllBlog
import WebSend


def Get() -> list[dict]:
    print('Process Rss')
    AllBlog = GetAllBlog.Get()

    CommentList = list()
    for BlogInfo in AllBlog:

        BlogTitle = BlogInfo['title']
        BlogLink = BlogInfo['link']

        print('Process', BlogTitle)
        PageContent = WebSend.Send(Url=BlogLink)

        # format to comments
        PostPage = BeautifulSoup(PageContent, 'html.parser')
        PostPage_Comments = PostPage.find('div', {'id': 'comments'})
        PostPage_Comments = PostPage_Comments.find('ol', {'class': 'comment-list'})
        PostPage_Comments = PostPage_Comments.find_all('li', {'class': 'comment-item'})

        OneCommentList = list()
        for OneComment in PostPage_Comments:
            VisitorInfo = dict()
            VisitorInfo['visitor'] = dict()
            VisitorInfo['comment'] = dict()

            # get avatar link
            div_avatar = OneComment.find('div', {'class': 'comment-item-avatar'})
            avatar = div_avatar.find('img')
            avatar = avatar['src']
            VisitorInfo['visitor']['avatar'] = avatar

            # get visitor name
            div_visitor = OneComment.find('div', {'class': 'comment-item-title'})
            visitor_name = div_visitor.find('div', {'class': 'comment-author'})
            visitor_name = visitor_name.text
            VisitorInfo['visitor']['name'] = visitor_name

            # get visitor platform
            div_visitor = OneComment.find('div', {'class': 'comment-item-title'})
            visitor_platform = div_visitor.find('div', {'class': 'comment-useragent'})
            visitor_platform = visitor_platform.text
            VisitorInfo['visitor']['platform'] = visitor_platform[2:]

            # get comment date div
            div_comment = OneComment.find('div', {'class': 'comment-item-title'})
            comment_time = div_comment.find('div', {'class': 'comment-time'})

            # short time
            comment_short_time = comment_time.find('span', {'class': 'human-time'})
            comment_short_time = comment_short_time.text
            VisitorInfo['comment']['short-time'] = comment_short_time

            # full time
            comment_full_time = comment_time.find('div', {'class': 'comment-time-details'})
            comment_full_time = comment_full_time.text
            VisitorInfo['comment']['time'] = comment_full_time

            # get comment text
            div_comment = OneComment.find('div', {'class': 'comment-item-text'})
            comment_content = div_comment.find('p')
            comment_content = comment_content.text
            VisitorInfo['comment']['content'] = comment_content

            # add item
            OneCommentList.append(VisitorInfo)

        # add item
        CommentList.append({BlogTitle: OneCommentList})

    return CommentList
