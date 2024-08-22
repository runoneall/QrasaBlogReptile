from bs4 import BeautifulSoup
import WebSend


def Get(Url:str) -> int:
    PageContent = WebSend.Send(Url=Url)

    # format to article
    PostPage = BeautifulSoup(PageContent, 'html.parser')
    PostPage_Article = PostPage.find('main', {'id': 'main'})
    PostPage_Article = PostPage_Article.find_all('article', id=lambda x: x and x.startswith('post-'))

    # get id
    PostPage_Article = PostPage_Article[0]
    PostId = PostPage_Article['id']
    PostId = PostId[5:]
    return int(PostId)