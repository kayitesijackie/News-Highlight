import urllib.request,json
from .models import Source,Article
from app import app

# Getting api key
# api_key = None
# # Getting the news base url
# source_base_url = None
# articles_base_url = None

# def configure_request(app):
#     global api_key,source_base_url,articles_base_url
api_key = app.config['NEWS_API_KEY']
source_base_url = app.config['NEWS_SOURCES_BASE_URL']
articles_base_url = app.config['NEWS_ARTICLES_API_BASE_URL']

def get_sources(category):
    '''Function that gets json response to our url request'''
    get_sources_url = source_base_url.format(category,api_key)
    

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    Function that processes the source result and transform to a list of objects

    Args:
        source_list: A list of dictionaries that contain news sources

    Returns:
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')

        source_object = Source(id,name,description)
        source_results.append(source_object)

    return source_results

def get_articles(id):
    '''Function thet gets the json response to our url request'''
    get_articles_url = articles_base_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)

    return article_results

def process_articles(article_list):
    '''
    Function that processes the airticle result and transforms them to a list of objects

    Args:
        article_list: a list of dictionaries that contain articles

    Returns:
        article_results: a list of article objects

    '''
    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        title = article_item.get('title')
        author= article_item.get('author')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')
        if urlToImage:
            article_object = Article(id,title,author,description,url,urlToImage,publishedAt,content)
            article_results.append(article_object)

    return article_results




#....