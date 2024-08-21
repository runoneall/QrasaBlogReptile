# Get Site About

from bs4 import BeautifulSoup
import WebSend
import Config
import WriteFile


def Get():
    AuthorInfo = dict()
    AuthorInfo['assets'] = dict()

    # Process Blog About
    PageContent = WebSend.Send(Url=Config.BlogAbout)
    PageContent = BeautifulSoup(PageContent, 'html.parser')

    PageContent = PageContent.find('div', {'id': 'post_content'})
    AboutContent = PageContent.find_all('p')

    AboutText = str()
    for Line in AboutContent:
        AboutText += Line.text
        AboutText += ' '

    AuthorInfo['site-about'] = AboutText

    # Process Author Card
    PageContent = WebSend.Send(Url=Config.Blog)
    PageContent = BeautifulSoup(PageContent, 'html.parser')

    AuthorCard = PageContent.find('div', {'id': 'leftbar_tab_overview'})

    # author name
    AuthorName = AuthorCard.find('h6', {'id': 'leftbar_overview_author_name'})
    AuthorInfo['author'] = AuthorName.text
    
    # slogan
    Slogan = AuthorCard.find('h6', {'id': 'leftbar_overview_author_description'})
    AuthorInfo['slogan'] = Slogan.text

    # assets
    div_assets = AuthorCard.find('nav', {'class': 'site-state'})
    
    # posts assets
    div_posts = div_assets.find('div', {'class': 'site-state-posts'})
    div_posts = div_posts.find('span', {'class': 'site-state-item-count'})
    AuthorInfo['assets']['posts'] = div_posts.text

    # categories assets
    div_categories = div_assets.find('div', {'class': 'site-state-categories'})
    div_categories = div_categories.find('span', {'class': 'site-state-item-count'})
    AuthorInfo['assets']['categories'] = div_categories.text

    # tags assets
    div_tags = div_assets.find('div', {'class': 'site-state-tags'})
    div_tags = div_tags.find('span', {'class': 'site-state-item-count'})
    AuthorInfo['assets']['div_tags'] = div_tags.text

    # return
    return AuthorInfo